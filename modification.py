
# Modifier data dans la BDD
def modification_plante_bdd(mycursor, mydb):

    choix_plante = input("Quelle plante souhaitez-vous modifier ? : ")
    champ = ""
    choix_champ = input("Que souhaitez vous modifier ? (N)om, (I)ndication, Partie (U)tilisée, (P)rix : ").upper()
    if choix_champ == "N":
        champ = "nom"
    if choix_champ == "I":
        champ = "indication"
    if choix_champ == "U":
        champ = "partie_utilisee"
    if choix_champ == "P":
        champ = "prix"
    nouvelle_data = input("Entrez la nouvelle valeur à affecter : ")
    if not isinstance(nouvelle_data, int):
        nouvelle_data = '\'' + nouvelle_data + '\''
    commande = str("UPDATE plante SET " + champ + " = " + nouvelle_data + " WHERE nom = " + "\"" + choix_plante + "\"")
    mycursor.execute(commande)
    mydb.commit()


