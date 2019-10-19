import sqlite3

existing_tables = ['recepies','clients','favourites']
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

    def query(self, table: str, sql: str):
        if table in existing_tables:
            connection = sqlite3.connect('cook_ass_db')
            cursor = connection.cursor()
            try:
                cursor.execute(sql)
            except sqlite3.IntegrityError as err: print(err)     
            ans = cursor.fetchall()
            connection.commit()
            connection.close()
        else: print('There is no such table')   
        return ans

    def insert_many(self, table: list, values: list):
        if table in existing_tables:
            connection = sqlite3.connect('cook_ass_db')
            cursor = connection.cursor()
            
            if (table == "recepies"):
                try:
                    cursor.executemany("INSERT INTO recepies VALUES (?,?,?,?,?)", values)
                except sqlite3.IntegrityError as err: print(err)   

            if (table == "clients"):
                try:
                    cursor.executemany("INSERT INTO clients VALUES (?,?)", values)
                except sqlite3.IntegrityError as err: print(err)

            if (table == "favourites"):
                try:
                    cursor.executemany("INSERT INTO favourites VALUES (?,?,?)", values)
                except sqlite3.IntegrityError as err: print(err)

            connection.commit()
            connection.close()
        else: print('There is no such tables')
              
    

    

