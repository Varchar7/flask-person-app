import sqlite3

from tomlkit import table


class DatabaseService():
    def __init__(self):
        self.database = sqlite3.connect(
            "database.sqlite3.db", check_same_thread=False)

    def create_table(self, table_name):
        self.table_name = table_name
        # self.database.execute(
        #     f"CREATE TABLE {table_name} (ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,EMAIL TEXT,AGE INT ,MOBILE_NUMBER TEXT) ")

    def insert(self, name, email, age, number):
        query = f" INSERT INTO {self.table_name}(NAME,EMAIL,AGE,MOBILE_NUMBER) VALUES('{name}','{email}','{age}','{number}');"
        self.database.execute(query)

    def select(self):
        return self.database.execute(f"SELECT * FROM {self.table_name};").fetchall()

    def commit(self):
        self.database.commit()

    def dispose(self):
        self.database.close()
