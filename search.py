# Search in Database
def search_bdd(mycursor, mydb):
    while True:
        mycursor2 = mycursor
        choix = input("Voulez-vous rechercher par (N)om ou par (I)D ? (P)récédent : ").upper()
        if choix == 'N':
            search = input("Entrez-votre recherche : ")
            search = '\'' + search + '\''
            mycursor.execute("SELECT * FROM plante WHERE INSTR(upper(nom), {})ORDER BY nom ASC, prix DESC LIMIT 3".format(search.upper()))
            myresult = mycursor.fetchall()
            break
        elif choix == 'I':
            search = input("Entrez tout ou partie de l'id de la plante recherchée : ")
            mycursor.execute("SELECT * FROM plante WHERE INSTR(id, {})".format(search))
            myresult = mycursor.fetchall()
            break
        elif choix == 'P':
            return
        else:
            print("Entrée invalide. Recommencez.")

    for i in myresult:
        print(i)


