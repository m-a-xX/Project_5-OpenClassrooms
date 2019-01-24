"""This file call the functions writen in other files"""

import categories
import products
import display

categories.create_db()
categories.add_cats()
products.load_products()
display.menu()
