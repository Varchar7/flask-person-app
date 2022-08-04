import sqlite3
import uuid


class DatabaseService():
    def __init__(self):
        self.database = sqlite3.connect(
            "database.sqlite3.db", check_same_thread=False)

    def create_table(self, table_name):
        self.table_name = table_name
        self.database.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} (ID TEXT PRIMARY KEY,NAME TEXT,EMAIL TEXT,AGE INT ,MOBILE_NUMBER TEXT) ")

    def insert(self, name, email, age, number):
        uid = uuid.uuid4()
        query = f" INSERT INTO {self.table_name} VALUES('{uid}','{name}','{email}','{age}','{number}');"
        self.database.execute(query)

    def update(self, id, name, email, age, number):
        fields = [('NAME', name), ('EMAIL', email),
                  ('AGE', age), ('MOBILE_NUMBER', number)]
        for field in fields:
            query = f"UPDATE {self.table_name} SET {field[0]}='{field[1]}' WHERE ID = '{id}'"
            self.database.execute(query)

    def select(self):
        return self.database.execute(f"SELECT * FROM {self.table_name};").fetchall()

    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE ID = '{id}'"
        self.database.execute(query)
        return self.select()

    def get_by_id(self, id):
        return self.database.execute(f"SELECT * FROM {self.table_name} WHERE ID = '{id}';").fetchone()

    def commit(self):
        self.database.commit()

    def dispose(self):
        self.database.close()
