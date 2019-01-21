'''File that manage the display of menu and substituts'''

import sys
import random
import mysql.connector

import reg_products
from categories import CATS


def menu():
    '''Print the menu and the products of the choosen category'''
    print('\n')
    print('\n')
    print("Bienvenue dans le programme de PurBeurre, nous vous proposons \
de trouver des substitus plus sains aux produits que vous consommez \
regulièrement. Pour cela, sélectionnez une catégorie en entrant le chiffre \
correspondant, puis sélectionnez un produit, toujours en entrant le chiffre \
associé. Vous pouvez aussi retrouver les produits que vous avez enregistrés \
auparavant\nA CHAQUE FOIS QU'IL VOUS SERA DEMANDÉ DE FAIRE UN CHOIX, VEUILLEZ \
ENTRER UN NOMBRE.\n")
    f_c = 6
    try:
        f_c = int(input("Voulez-vous consulter :\n1 : les produits des 5 \
catégories choisies\n2 : les produits que vous avez enregistrés précedemment\
\n"))
    except ValueError:
        while f_c != 1 and f_c != 2:
            try:
                f_c = int(input("Voules vous consulter :\n1 : les produits des \
5 catégories choisies\n2 : les produits que vous avez enregistrés précedemment\
\n"))
            except ValueError:
                f_c = int(input("Voules vous consulter :\n1 : les produits des \
5 catégories choisies\n2 : les produits que vous avez enregistrés précedemment\
\n"))
    while f_c != 1 and f_c != 2:
        f_c = int(input("Voulez-vous consulter :\n1 : les produits des 5 \
catégories choisies\n2 : les produits que vous avez enregistrés précedemment\
\n"))
    print('\n')
    if f_c == 1:
        for i in range(0, 5):
            print((i + 1), " - ", CATS[i])
            print('\n')
        c_c = 6
        try:
            c_c = int(input("Les produits de quelle catégorie voulez-vous \
afficher ?\n"))
        except ValueError:
            while c_c != 1 and c_c != 2 and c_c != 3 and c_c != 4 and c_c != 5:
                try:
                    c_c = int(input("Les produits de quelle catégorie voulez-\
vous afficher ? Merci d'entrer un chiffre.\n"))
                except ValueError:
                    c_c = int(input("Les produits de quelle catégorie voulez-\
vous afficher ? Merci d'entrer un chiffre.\n"))
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
        product()
    if f_c == 2:
        reg_products.display_reg()
        c_m = input("\nVeuillez appuyer sur ENTREE pour retourner au menu\n")
        if c_m != 0:
            menu()


def product():
    i = 0
    '''Choose a product and print a substitut'''
    c_p = 5001
    try:
        c_p = int(input("\nQuel produit voulez vous remplacer par un \
produit plus sain ?\n"))
    except ValueError:
        while c_p < 0 or c_p > 5000:
            try:
                c_p = int(input("\nQuel produit voulez vous remplacer par un \
produit plus sain ? Merci d'entrer un nombre.\n"))
            except ValueError:
                c_p = int(input("\nQuel produit voulez vous remplacer par un \
produit plus sain ? Merci d'entrer un nombre.\n"))
    while c_p < 0 or c_p > 5000:
        c_p = int(input("\nQuel produit voulez vous remplacer par un \
produit plus sain ?\n"))
    try:
        conn = mysql.connector.connect(host="localhost", user="maxence",\
                                       password="maxence", database="P5")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT Categories_id FROM Products WHERE \
                        id = %s" % (c_p))
        cat_dat = cursor.fetchall()
        cursor.execute("SELECT name, shop, url, description, id FROM Products \
                        WHERE Categories_id = %s AND nutrition_grade = 'a'" % \
                        (cat_dat[0]))
        data = cursor.fetchall()
        for row in data:
            i += 1
        n = random.randint(0, i)
        count = 0
        for row in data:
            if n == count:
                print("\nSUBSTITUT :\nNom :", row[0], "\nMagasin(s) :", \
                       row[1], "\nURL :", row[2], "\nDescription :", row[3])
                reg_id = row[4]
            count += 1
    except mysql.connector.errors.InterfaceError as error:
        print("Error %d: %s" % (error.args[0], error.args[1]))
        sys.exit(1)
    try:
        reg = int(input("\nVoulez-vous enregistrer ce produit pour pouvoir le \
consulter plus tard ?\nNon : 0\nOui : 1\n"))
    except ValueError:
        while reg != 0 and reg != 1:
            try:
                reg = int(input("\nVoulez-vous enregistrer ce produit pour \
pouvoir le consulter plus tard ?\nNon : 0\nOui : 1\n"))
            except ValueError:
                reg = int(input("\nVoulez-vous enregistrer ce produit pour \
pouvoir le consulter plus tard ?\nNon : 0\nOui : 1\n"))
    while reg != 0 and reg != 1:
         reg = int(input("\nVoulez-vous enregistrer ce produit pour pouvoir le \
consulter plus tard ?\nNon : 0\nOui : 1\n"))
    if reg == 1:
        reg_products.reg(reg_id)
    menu()