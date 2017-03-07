import mysql.connector
from mysql.connector import errorcode

from fabItems import numbers as fnumbers
from fabItems import prices as fprices
from fabItems import links as flinks
from fabItems import names as fnames

fixedNumbers = []
fixedPrices = []
fixedNames = []

for x, y, z in zip(fnumbers, fprices, fnames):
    fixedNumbers.append(str(x))
    fixedPrices.append(str(y))
    s = z.replace(u'\xae', u'')
    ss = s.replace(u'\u2122', u'')
    name = ss.replace("'", '')
    fixedNames.append(str(name))

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
  query = ("SELECT * FROM fabItems")
  try:
    cursor.execute(query)
  except mysql.connector.Error as er:
    error = str(er)
    if error[-13 : ] == "doesn't exist":
      print('Table currently ' + error[-13 : ] + '.')
      fabTable = ("CREATE TABLE `fabItems` ( `row_no` int(11) KEY NOT NULL AUTO_INCREMENT, `itemSupplier` VARCHAR(75), `itemNumber` VARCHAR(20), `itemPrice` VARCHAR(9), `itemLink` VARCHAR(100), `itemName` VARCHAR(1000))")
      cursor.execute(fabTable)
      print('Table for Fab-Ent has been created.' + '\n' + 'Starting to populate the table.')
      
      for x, y, z, s in zip(fixedNumbers, fixedPrices, flinks, fixedNames):
        fabInsertion = "INSERT INTO fabItems (`row_no`, `itemSupplier`, `itemNumber`, `itemPrice`, `itemLink`, `itemName`) VALUES (NULL, 'FAB', '" + x + "', '" + y + "', '" + z + "', '" + s + "')"
        cursor.execute(fabInsertion)
      
  else:
    rmTable = ('DROP TABLE fabItems')
    cursor.execute(rmTable)
    print('Table Removed')
    
  cnx.commit()
  cursor.close()
  cnx.close