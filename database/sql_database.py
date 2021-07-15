import sqlite3
from sqlite3.dbapi2 import Error

class Sql_Database:
    
    def __init__(self, name):
        try:
            self._conn = sqlite3.connect(name)
            self._cursor = self._conn.cursor()
        except Error:
            print(Error)

    def close(self):
        self._conn.close()
    
    def create_table(self,table):
        self._cursor.execute("CREATE TABLE ")

    def insert_into_table(self,table,columns,data):
        self._cursor.execute("INSERT INTO {0} ({1}) VALUES ({2});".format(table,columns,data))

    def commit(self):
        self._conn.commit()