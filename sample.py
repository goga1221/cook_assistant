import sqlite3
from db_class import *
from parse_url import *

cs_db = DB() 
cs_db.create_db()
tuple01 = (['name testdasgbvsdbdsgaew\n 01', 'catadf\naew wrqaww test 01','receawdawpie 01','соль,awdad,aw dawd\ndawd,'],)
cs_db.insert_many('recepies', tuple01)

