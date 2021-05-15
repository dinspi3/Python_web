
import mysql.connector

mydb = mysql.connector.connect(
  host="sql11.freesqldatabase.com",
  user="sql11412534",
  password="TIpV6ltJk8",
  database="sql11412534"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Person")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)