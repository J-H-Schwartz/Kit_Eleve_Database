# Read Database
def read_bdd(mycursor, mydb):
    mycursor.execute("SELECT * FROM plante")
    myresult = mycursor.fetchall()

    for i in myresult:
        print(i)
