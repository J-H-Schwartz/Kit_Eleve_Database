import mysql.connector
from modification import modification_plante_bdd as mod
from insert import insertion_nouvelle_ligne as insert
from read import read_bdd
from delete import delete_ligne_bdd
from search import *

mydb = mysql.connector.connect(
    host="localhost",
    user="jonathan",
    passwd="29072015aA",
    database="herboristerie"
)
mycursor = mydb.cursor()


def main():
    while True:
        choix = input("Que souhaitez-vous-faire ? (A)fficher BDD, (I)nserer une ligne, (M)odifier ligne, (S)upprimer,"
                      "(R)echercher, (Q)uitter").upper()
        if choix == 'Q':
            break
        elif choix == 'A':
            read_bdd(mycursor, mydb)
        elif choix == 'M':
            mod(mycursor, mydb)
        elif choix == 'I':
            insert(mycursor, mydb)
        elif choix == 'S':
            delete_ligne_bdd(mycursor, mydb)
        elif choix == 'R':
            search_bdd(mycursor, mydb)
        else:
            print("Entrée non reconnue. Recommencez.")


if __name__ == '__main__':
    main()
