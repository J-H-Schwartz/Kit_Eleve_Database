# Read Database
def search_bdd(mycursor, mydb):

    choix = input("Voulez-vous rechercher par (N)om ou par (I)D ? : ").upper()
    if choix == 'N':
        search = input("Entrez-votre recherche : ")
        search = '\'' + search + '\''
        mycursor.execute("SELECT * FROM plante WHERE INSTR(upper(nom), {})".format(search.upper()))
        myresult = mycursor.fetchall()
    elif choix == 'I':
        search = input("Entrez tout ou partie de l'id de la plante recherchée : ")
        mycursor.execute("SELECT * FROM plante WHERE INSTR(id, {})".format(search))
        myresult = mycursor.fetchall()

    for i in myresult:
        print(i)
