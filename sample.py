import sqlite3
from db_class import *
from parse_url import *

cs_db = DB() 
cs_db.create_db()
print("{795726498: 'g0ga_nik'}")
print(cs_db.client_subscription(479236808, 'NiceParadiss'))
id = 479236808
name = 'NiceParadiss'
cs_db.query(f"INSERT INTO clients (id, name) values ({id},'{name}')")
print(cs_db.query(f"SELECT * FROM clients WHERE name = ('{name}') AND id = {id}"))

