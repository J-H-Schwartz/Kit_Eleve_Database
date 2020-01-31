def delete_ligne_bdd(mycursor, mydb):

    nom_entree_a_supprimer = input("Entrez le nom ou l'id d'une plante à supprimer du tableau :")
    mycursor.execute("DELETE FROM plante WHERE nom = \'{}\'".format(nom_entree_a_supprimer))
    mydb.commit()
