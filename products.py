'''File that manage the products importation'''

import requests
import mysql.connector

from categories import CATS
from conf import SQL_LOG, SQL_PWD


def load_products():
    '''Import products from API and add them in the database'''
    print("Importation des produits...")
    nbr = 0
    for i in range(0, 5):
        payload = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': CATS[i],
            'countries': 'France',
            'page_size': '1000',
            'json': 1
            }
        reponse = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', \
                               params=payload)
        data = reponse.json()
        try:
            conn = mysql.connector.connect(host="localhost", user=SQL_LOG,\
                                           password=SQL_PWD, database="P5")
            cursor = conn.cursor()
            for product in data['products']:

                try:
                    name = product['product_name_fr']
                except KeyError:
                    try:
                        name = product['product_name']
                    except KeyError:
                        pass
                try:
                    store = product['stores']
                except KeyError:
                    pass
                try:
                    description = product['generic_name_fr']
                except KeyError:
                    try:
                        description = product['generic_name']
                    except KeyError:
                        pass
                try:
                    nutrition_grade = product['nutrition_grade_fr']
                except KeyError:
                    try:
                        nutrition_grade = product['nutrition_grade']
                    except KeyError:
                        pass
                url = product['url']
                atts = (name, nbr, nutrition_grade, store, url, \
                        description, (i + 1))
                cursor.execute("INSERT IGNORE Products (name, id, \
                                nutrition_grade, shop, url, description, \
                                Categories_id) \
                                VALUES (%s, %s, %s, %s, %s, %s, %s)", atts)
                nbr += 1
            conn.commit()
            cursor.close()
        except KeyError:
            pass
        except mysql.connector.errors.IntegrityError:
            pass
        print("Importaion des produits de la catégorie %s réussie" % (i + 1))
