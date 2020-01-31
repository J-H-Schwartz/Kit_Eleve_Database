# Add row and data to Database
def insertion_nouvelle_ligne(mycursor, mydb):

    id_nouvelle_plante = input("Entrez l'id de la nouvelle plante : ")
    nouvelle_plante = input("Entrez le nom de la plante que vous souhaitez ajouter : ")
    indication_nouvelle_plante = input("Entrez l'indication de la plante : ")
    partie_utilisee_nouvelle_plante = input("Entrez la partie de la plante utilisée : ")
    prix_nouvelle_plante = input("Entrez le prix de la nouvelle plante : ")

    mycursor.execute("INSERT INTO plante (id, nom, indication, partie_utilisee, prix) "
                     "VALUES ('{}', '{}', '{}', '{}', '{}')".format(id_nouvelle_plante, nouvelle_plante,
                                                                    indication_nouvelle_plante,
                                                                    partie_utilisee_nouvelle_plante,
                                                                    prix_nouvelle_plante))
    mydb.commit()
