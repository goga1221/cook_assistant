import sqlite3
from db_class import *
from parse_url import *

cs_db = DB() 
cs_db.create_db()

#cs_db.add_to_favourites(479236808, 'перловка с говядиной')
#cs_db.add_to_favourites(479236808, '"зубы вампира" из яблок и конфет')
#cs_db.add_to_favourites(777, '"зубы вампира" из яблок и конфет')
#print(cs_db.get_favourites(479236808))

ingredients = 'Хлеб соль'
ingredients_list = []
for i in ingredients.split(' '):    
    i = i.title()
    print(i)
    ingredients_list.append(i)
ingr_list1 = ['мука молоко яйца']
ingr_list2 = ['Майонез','Сметана']
print(cs_db.get_recepie_by_ingredients(ingredients_list))
print(cs_db.get_recepie_by_ingredients(ingr_list2))

recepie = ['Пирогпиронг','тесто, песто, кресло','оставь тесто и песто, сядь на кресло, расслабься и получай удовольствие']
cs_db.add_recepie(479236808, recepie)