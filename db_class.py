import sqlite3

class DB:
    def __init__(self):
        """Constructor"""
        pass
    
    def create_db(self):
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()

        try:
            cursor.execute( """CREATE TABLE recepies 
         (id integer PRIMARY KEY, name text, category text, recepie text, ingridients text)""")
        except sqlite3.OperationalError: print('table recepies already exists')  

        try:
            cursor.execute("""CREATE TABLE clients
         (id integer PRIMARY KEY, name text)""")
        except sqlite3.OperationalError: print('table clients already exists')

        try:
            cursor.execute("""CREATE TABLE favourites
         (id integer PRIMARY KEY, id_client integer, id_recepie integer, clients_recepie boolean, 
      FOREIGN KEY (id_client) REFERENCES clients(id), FOREIGN KEY (id_recepie) REFERENCES recepies(id))""")
        except sqlite3.OperationalError: print('table favourites already exists')  

        connection.commit()
        connection.close()

    def query(self, sql: str):
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()
        cursor.execute(sql)
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        return ans

    def insert_many(self, table: str, values: list):
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()
        if (table == "recepies"):
            cursor.executemany("INSERT INTO recepies VALUES (?,?,?,?,?)", values)
        if (table == "clients"):
            cursor.executemany("INSERT INTO clients VALUES (?,?)", values)
        if (table == "favourites"):
            cursor.executemany("INSERT INTO favourites VALUES (?,?,?)", values)
        connection.commit()
        connection.close()
              
    

    

