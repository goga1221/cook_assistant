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
         (id integer PRIMARY KEY AUTOINCREMENT , name text, category text, recepie text, ingredients text)""")
        except sqlite3.OperationalError: print('table recepies already exists')  

        try:
            cursor.execute("""CREATE TABLE clients
         (id integer PRIMARY KEY AUTOINCREMENT , name text)""")
        except sqlite3.OperationalError: print('table clients already exists')

        try:
            cursor.execute("""CREATE TABLE favourites
            (id integer PRIMARY KEY AUTOINCREMENT , id_client integer, id_recepie integer, clients_recepie boolean,             
            UNIQUE(id_client,id_recepie),
            FOREIGN KEY (id_client) REFERENCES clients(id), FOREIGN KEY (id_recepie) REFERENCES recepies(id))""")
        except sqlite3.OperationalError: print('table favourites already exists')  

        connection.commit()
        connection.close()

    def query(self, sql: str):
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()
        try:
            cursor.execute(sql)
        except sqlite3.IntegrityError as err: print(err)     
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        return ans

    def insert_many(self, table: list, values: list):
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()
        existing_tables = {'recepies' : 4,'clients' : 1 ,'favourites': 2}
        tables_col = {'recepies' : 'name, category,recepie,ingredients','clients' : 'name' ,'favourites': 'id_client, id_recepie'} 
        if table in existing_tables:
            try:
                query = f"INSERT INTO {table} ({tables_col[table]}) VALUES ({','.join('?' for i in range(existing_tables[table]))})"
                cursor.executemany(query, values)
            except sqlite3.IntegrityError as err: print(err)
        connection.commit()
        connection.close()

    def get_random_recepie(self):
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()
        try:
            cursor.execute("""SELECT name, category, recepie, ingredients FROM recepies ORDER BY RANDOM() LIMIT 1""")
        except sqlite3.IntegrityError as err: print(err)     
        ans = cursor.fetchone()
        connection.commit()
        connection.close()
        return ans

    def get_favourites(self, client: str):
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT name, category, recepie, ingredients FROM recepies WHERE id in \
            (SELECT id_recepie FROM favourites WHERE id_client = \
            (SELECT id FROM clients WHERE name = '{client}'))")
        except sqlite3.IntegrityError as err: print(err)     
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        return ans

    def get_recepie_by_name(self, rec_name: str):        
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT name, category, recepie, ingredients FROM recepies WHERE name LIKE '%{rec_name}%'")
        except sqlite3.IntegrityError as err: print(err)     
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        return ans

    def get_recepie_by_ingredients(self, ingredients_list: list):
        connection = sqlite3.connect('cook_ass_db')
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT name, category, recepie, ingredients FROM recepies \
                 WHERE ingredients LIKE '%{'%'.join(ingredients_list)}%'")
        except sqlite3.IntegrityError as err: print(err)     
        ans = cursor.fetchall()
        connection.commit()
        connection.close()
        return ans

