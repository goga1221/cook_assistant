import sqlite3
from db_class import *
from parse_url import *

cs_db = DB() 
cs_db.create_db()
print(cs_db.get_recepie_by_name('бутерброд'))
print(cs_db.get_recepie_by_ingredients(['хлеб, соль']))
"""tuple01 = (['name testdasgbvsdbdsgaew\n 01', 'catadf\naew wrqaww test 01','receawdawpie 01','соль,awdad,aw dawd\ndawd,'],)
cs_db.insert_many('recepies', tuple01)
 cs_db.query("INSERT INTO clients (name) values ('Ivan')")
cs_db.query("INSERT INTO recepies (name) values ('test recepie')")
cs_db.query("INSERT INTO favourites (id_client, id_recepie) values (1, 1)")
cs_db.query("INSERT INTO favourites (id_client, id_recepie) values (1, 1)")
print(cs_db.query('SELECT * FROM clients'))
clients_list = (['Vasya'], ['Petya'])
cs_db.insert_many('clients', clients_list) 
touple = (['Корейский салат с редькой, морковью и куриными потрошками', 'категория', '\n1) Подготовьте продукты для салата. Лук, чеснок, имбирь, морковь и редьку почистите, помойте, обсушите. Для салата можно использовать как дайкон, так и черную редьку.\n2) Куриные желудки или сердечки промойте и отварите до готовности в чуть подсоленной воде (20-30 минут).\n3) Редьку и морковь натрите на терке для корейской моркови, сложите в удобную глубокую миску.\n4) Салатный лук и острый перец нарежьте тонкой соломкой. Чеснок и имбирь натрите на мелкой терке. Добавьте к моркови с редькой.\n5) Куриные желудки остудите, срежьте с них жилистые соединения, нарежьте соломкой и добавьте к остальным ингредиентам.\n6) Салат с редькой, морковью и куриными желудочками заправьте соевым соусом. Добавьте лимонный сок или белый винный уксус, поперчите, посолите по вкусу, добавьте кориандр (разотрите его между пальцами).\n7) Кунжутное масло раскалите в маленькой сковородке или разогрейте в микроволновке 1,5-2 минуты. Залейте горячим маслом салат, перемешайте и дайте ингредиентам салата промариноваться и пропитаться всеми вкусами.\n8) Готовый корейский салат с редькой, морковью и куриными потрошками посыпьте кунжутными семечками и подавайте к столу.', 'Куриные желудки или сердечки - 300 г, Редька черная или дайкон - 150 г, Морковь - 1 шт., Лук репчатый салатный - 0,5 шт., Перец чили свежий - по вкусу, Чеснок - 1-2 зубчика, Имбирь, свежий корень - 1 см, Соус соевый - 2-3 ст. л., Сок лимона (или уксус винный белый)- 1-2 ст. л., Масло кунжутное - 2 ст. л., Кориандр в зернах - 0,5 ч. л., Кунжутные семена - 1 ч. л., Соль морская - по вкусу, Перец черный молотый - по вкусу'])"""

""" 
print(cs_db.query('SELECT * FROM clients WHERE id=1'))
cs_db.query("INSERT INTO recepies (name, category, recepie, ingredients) VALUES ('name test 1', 'cat test 1','recepie 1','мука, соль')")
cs_db.query("INSERT INTO recepies (name, category, recepie, ingredients) VALUES ('name test 2', 'cat test 2','recepie 2','вода, сахар')")
cs_db.query("INSERT INTO recepies (name, category, recepie, ingredients) VALUES ('name test 3', 'cat test 3','recepie 3','топор, каша, любовь')")
print(cs_db.get_random_recepie())
print(cs_db.get_favourites("Ivan"))
print(cs_db.get_recepie_by_name('name test 3'))
print(cs_db.get_recepie_by_ingredients(['соль']))
print(cs_db.get_recepie_by_ingredients(['соль','вода']))
print(cs_db.get_recepie_by_ingredients(['топор','любовь']))
 """
