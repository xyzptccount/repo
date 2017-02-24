import mysql.connector
from mysql.connector import errorcode
from mmItems import numbers
from mmItems import prices
from mmItems import links

try:
  cnx = mysql.connector.connect(user='root', password="patriots", database='pt_db')
  #cnx = mysql.connector.connect(user='dvitt90', database='c9')
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
  query = ("SELECT * FROM mmPriceDB")
  try:
    cursor.execute(query)
  except mysql.connector.Error as er:
    error = str(er)
    if error[-13 : ] == "doesn't exist":
      print('Table currently ' + error[-13 : ] + '.')
      createTable = ("CREATE TABLE `mmPriceDB` ( `row_no` int(11) KEY NOT NULL AUTO_INCREMENT, `itemNumber` VARCHAR(20), `itemPrice` VARCHAR(9), `itemLink` VARCHAR(50))")
      cursor.execute(createTable)
      print('Table for Milliken Medical has been created.' + '\n' + 'Starting to populate the table.')
      for x, y, z in zip(numbers, prices, links):
        insertion = "INSERT INTO mmPriceDB (`row_no`, `itemNumber`, `itemPrice`, `itemLink`) VALUES (NULL, '" + x + "', '" + y + "', '" + z + "')"
        cursor.execute(insertion)
      
  else:
    rmTable = ('DROP TABLE mmPriceDB')
    cursor.execute(rmTable)
    print('Table Removed')
    
  cnx.commit()
  cursor.close()
  cnx.close
