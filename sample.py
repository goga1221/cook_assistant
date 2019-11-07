import sqlite3
from db_class import *
from parse_url import *

cs_db = DB() 
cs_db.create_db()

cs_db.client_subscription(479236808, 'NiceParadiss')