'''File that manage the registration of products on user asking'''

import sys
import mysql.connector

def reg(reg_id):
    try:
        conn = mysql.connector.connect(host="localhost", user="maxence",\
                                           password="maxence", database="P5")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT name, Categories_id, description, shop, \
                        url, nutrition_grade FROM Products \
                        WHERE id = %d" % (reg_id))
        data = cursor.fetchall()
        for row in data:
            name = row[0]
            cat_id = row[1]
            description = row[2]
            stores = row[3]
            url = row[4]
            nutrition_grade = row[5]
        atts = (name, reg_id, cat_id, description, stores, url, nutrition_grade)
        cursor.execute("INSERT IGNORE Registred_products (name, id, \
                        Categories_id, description, shop, url, \
                        nutrition_grade) VALUES (%s, %s, %s, %s, %s, %s, \
                        %s)", (atts))
    except mysql.connector.errors.InterfaceError as error:
        print("Error %d: %s" % (error.args[0], error.args[1]))
        sys.exit(1)

def display_reg():
    try:
        conn = mysql.connector.connect(host="localhost", user="maxence",\
                                       password="maxence", database="P5")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT name, shop, url, description FROM \
                        Registred_products")
        data = cursor.fetchall()
        count = 1
        for row in data:
            print("\nProduit ", count, "\nNom :", row[0], "\nMagasin(s) :", \
                   row[1], "\nURL :", row[2], "\nDescription :", row[3], "\n\n")
            count += 1
    except mysql.connector.errors.InterfaceError as error:
        print("Error %d: %s" % (error.args[0], error.args[1]))
        sys.exit(1)