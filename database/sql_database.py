import sqlite3

class Sql_Database:
    
    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    def close(self):
        self._conn.close()
    
    def create_table(self):
        self._conn.execute()

    def commit(self):
        self._conn.commit()