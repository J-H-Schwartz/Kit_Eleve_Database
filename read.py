import mysql.connector
from modification import modification_plante_bdd as mod
from insert import insertion_nouvelle_ligne as insert

mydb = mysql.connector.connect(
  host="localhost",
  user="jonathan",
  passwd="29072015aA",
  database="herboristerie"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM plante")
myresult = mycursor.fetchall()

for i in myresult:
    print(i)

mod(mycursor, mydb)
insert(mycursor, mydb)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM plante")
myresult = mycursor.fetchall()

for i in myresult:
    print(i)