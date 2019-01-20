'''File that manage the display of menu and substituts'''

import sys
import mysql.connector

from categories import CATS


def menu():
    '''Print the menu and the products of the choosen category'''
    print('\n')
    print('\n')
    print("Bienvenue dans le programme de PurBeurre, nous vous proposons \
de trouver des substitus plus sains aux produits que vous consommez \
regulièrement. Pour cela, sélectionnez une catégorie en entrant le chiffre \
correspondant, puis sélectionnez un produit, toujours en entrant le chiffre \
associé.\n")
    for i in range(0, 5):
        print((i + 1), " - ", CATS[i])
        print('\n')
    c_c = int(input("Les produits de quelle catégorie voulez-vous afficher ?\n"))
    while c_c != 1 and c_c != 2 and c_c != 3 and c_c != 4 and c_c != 5:
        c_c = int(input("Les produits de quelle catégorie voulez-vous \
                       afficher ?\n"))
    try:
        conn = mysql.connector.connect(host="localhost", user="maxence",\
                                       password="maxence", database="P5")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM Products WHERE \
                        Categories_id = %d" % (c_c))
        data = cursor.fetchall()
        for row in data:
            print(row[0], " : ", row[1])
    except mysql.connector.errors.InterfaceError as error:
        print("Error %d: %s" % (error.args[0], error.args[1]))
        sys.exit(1)
