import sqlite3
from db_class import *
from parse_url import *

cs_db = DB() 
cs_db.create_db()

cs_db.add_to_favourites(479236808, 'перловка с говядиной')
cs_db.add_to_favourites(479236808, '"зубы вампира" из яблок и конфет')
cs_db.add_to_favourites(777, '"зубы вампира" из яблок и конфет')
print(cs_db.get_favourites(479236808))

print(cs_db.get_recepie_by_ingredients(['Сметана','Майонез']))
print(cs_db.get_recepie_by_ingredients(['Майонез','Сметана']))
