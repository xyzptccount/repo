import mysql.connector
from mysql.connector import errorcode
from mmItems import numbers
from mmItems import prices
from mmItems import links
from mmItems import names

fixedNames = []
for x in names:
  fixedNames.append(str(x))

try:
  #cnx = mysql.connector.connect(user='root', password="Acidburn1", database='pt_db')
  cnx = mysql.connector.connect(user='dvitt90', database='c9')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print('DB Login Successful!!')
  cursor = cnx.cursor(buffered=True)
  query = ("SELECT * FROM priceDB")
  try:
    cursor.execute(query)
  except mysql.connector.Error as er:
    error = str(er)
    if error[-13 : ] == "doesn't exist":
      print('Table currently ' + error[-13 : ] + '.')
      millikenTable = ("CREATE TABLE `priceDB` ( `row_no` int(11) KEY NOT NULL AUTO_INCREMENT, `itemSupplier` VARCHAR(75), `itemNumber` VARCHAR(20), `itemPrice` VARCHAR(9), `itemLink` VARCHAR(100), `itemName` VARCHAR(1000))")
      cursor.execute(millikenTable)
      print('Table for Milliken Medical has been created.' + '\n' + 'Starting to populate the table.')
      
      for x, y, z, s in zip(numbers, prices, links, fixedNames):
        millikenInsertion = "INSERT INTO priceDB (`row_no`, `itemSupplier`, `itemNumber`, `itemPrice`, `itemLink`, `itemName`) VALUES (NULL, 'Milliken', '" + x + "', '" + y + "', '" + z + "', '" + s + "')"
        cursor.execute(millikenInsertion)
      
  
  else:
    rmTable = ('DROP TABLE priceDB')
    cursor.execute(rmTable)
    print('Table Removed')
    
  cnx.commit()
  cursor.close()
  cnx.close