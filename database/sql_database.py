import sqlite3
from sqlite3 import Error

class Sql_Database:
    
    def __init__(self, name):
        try:
            self._conn = sqlite3.connect(name)
            self._cursor = self._conn.cursor()
        except Error:
            print(Error)

    def close(self):
        self._conn.close()

    def commit(self):
        self._conn.commit()
    
    def create_table(self,table,columns):
        self._cursor.execute("CREATE TABLE {0} ({1})".format(table,columns))

    def drop_table(self,table):
        self._cursor.execute("DROP TABLE IF EXISTS {0} ".format(table))

    def insert_into_table(self,table,columns,data):
        self._cursor.execute("INSERT INTO {0} ({1}) VALUES ({2});".format(table,columns,data))
    
    def select_from_table(self,table,columns):
        self._cursor.execute("SELECT {0} FROM {1};".format(columns,table))
    
    def select_from_conditional(self,table,columns,condition):
        self._cursor.execute("SELECT {0} FROM {1} WHERE {2};".format(columns,table,condition))