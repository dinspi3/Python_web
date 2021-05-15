import mysql.connector

mydb = mysql.connector.connect(
  host="sql11.freesqldatabase.com",
  user="sql11412534",
  password="TIpV6ltJk8",
  database="sql11412534"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Person (`id`, `First_Name`, `Last_Name`, `Gender`, `Age`, `Tel`) VALUES (%s, %s,%s,%s,%s,%s)"
val = [
    ('4', 'www', 'wss', 'F', 20, 999999),
    ('5', 'ass', 'as', 'M', 21, 111111)

]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")