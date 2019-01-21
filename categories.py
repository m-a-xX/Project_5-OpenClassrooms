'''File that manage database and categories creation'''

import sys
import mysql.connector

with open('categories.sql') as f:
    CAT_CREATE = f.read()

with open('products.sql') as f:
    PRO_CREATE = f.read()

with open('reg_products.sql') as f:
    REG_CREATE = f.read()


def create_db():
    '''Create the database'''
    try:
        conn = mysql.connector.connect(host="localhost", user="maxence",\
                                       password="maxence")
        conn.autocommit = True
        cursor = conn.cursor()
        print("Création de la base de données...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS P5 \
                        DEFAULT CHARACTER SET 'utf8';")
        cursor.execute("USE P5")
        cursor.execute(CAT_CREATE)
        cursor.execute(PRO_CREATE)
        cursor.execute("CREATE INDEX IF NOT EXISTS `fk_Products_Categories_\
                        idx` ON `P5`.`Products` (`Categories_id` ASC);")
        cursor.execute(REG_CREATE)
        cursor.execute("CREATE INDEX IF NOT EXISTS `fk_Registred_products_\
                        Categories1_idx` ON `P5`.`Registred_products` \
                        (`Categories_id` ASC);")
        cursor.close()
        print("Base de données crée")
    except mysql.connector.errors.InterfaceError as error:
        print("Error %d: %s" % (error.args[0], error.args[1]))
        sys.exit(1)


CATS = ['Meals', 'Snacks', 'Non-Alcoholic beverages', 'Biscuits', 'Frozen foods']


def add_cats():
    '''Add categories in the database'''
    for i in range(0, 5):
        try:
            conn = mysql.connector.connect(host="localhost", user="maxence",\
                                           password="maxence", database="P5")
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(("INSERT IGNORE Categories (id, name) VALUES \
                (%(id)s, %(name)s)"), {"id": (i + 1), "name": CATS[i]})
        except mysql.connector.errors.InterfaceError as error:
            print("Error %d: %s" % (error.args[0], error.args[1]))
            sys.exit(1)
