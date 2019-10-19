from db_class import *

cs_db = DB() 
cs_db.create_db()
clients_list = [(2, 'Vasya'), (3,'Petya')]
cs_db.insert_many('clients', clients_list)
print(cs_db.query('clients','SELECT * FROM clients WHERE id=2'))