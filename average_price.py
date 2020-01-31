def average_price(mycursor, mydb):
    mycursor.execute("SELECT AVG(prix) FROM plante")
    myresult = mycursor.fetchall()
    print(myresult)
