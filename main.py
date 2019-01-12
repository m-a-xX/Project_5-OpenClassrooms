import json
import requests
import mysql.connector
import sys

#sql_create = open('DB_creation.sql', 'r') 
with open('DB_creation.sql') as f:
    sql_create = f.read()

try:
   conn = mysql.connector.connect(host="localhost", 
                                  user="maxence", password="maxhockey")

   cursor = conn.cursor()
   cursor.execute(sql_create, multi=True)

except mysql.connector.errors.InterfaceError as e:
   print("Error %d: %s" % (e.args[0],e.args[1]))
   sys.exit(1)


payload = {
    'action': 'process',
    'tagtype_0': 'categories',
    'tag_contains_0': 'contains',
    'tag_0': 'en:squeezed-juices',
    'countries': 'France',
    'page_size': '25',
    'json': 1
    }

reponse = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
data = reponse.json()

names = []
stores = []
url =[]

for product in data['products']:
    names.append(product['product_name_fr'])
    stores.append(product['stores'])
    url.append(product['url'])

for name in names:
    print(name)