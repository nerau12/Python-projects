import MySQLdb as mdb

class Database:
    
    def __init__(self):
        self.name = None
        self.conn = self.connect(db_name)
        self.cursor = self.conn.cursor()

    def connect(self):
        pass

    def __del__(self):
        self.cursor.close()
        self.conn.close()