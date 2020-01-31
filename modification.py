# Modifier data dans la BDD
def modification_plante_bdd(mycursor, mydb):

    choix_plante = input("Quelle plante souhaitez-vous modifier ? : ")
    champ = ""
    while True:
        choix_champ = input("Que souhaitez vous modifier ? (N)om, (I)ndication, Partie (U)tilisée, (P)rix : ").upper()
        if choix_champ == "N":
            champ = "nom"
            break
        elif choix_champ == "I":
            champ = "indication"
            break
        elif choix_champ == "U":
            champ = "partie_utilisee"
            break
        elif choix_champ == "P":
            champ = "prix"
            break
        elif choix_champ == "F":
            champ = "famille"
            break
        elif choix_champ == "FF":
            champ = "famille_fr"
            break
        elif choix_champ == "S":
            champ = "sous_classe"
            break
        elif choix_champ == "SF":
            champ = "sous_classe_fr"
            break
        else:
            print("Commande invalide. Recommencez.")
    nouvelle_data = input("Entrez la nouvelle valeur à affecter : ")
    if not isinstance(nouvelle_data, int):
        nouvelle_data = '\'' + nouvelle_data + '\''
    commande = str("UPDATE plante SET " + champ + " = " + nouvelle_data + " WHERE nom = " + "\"" + choix_plante + "\"")
    mycursor.execute(commande)
    mydb.commit()


