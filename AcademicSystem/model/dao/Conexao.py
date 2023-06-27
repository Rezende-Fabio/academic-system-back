import sqlite3
import sys

class Conexao:

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connected = None

    def conect(self):
        try:
            self.conn = sqlite3.connect("AcademicSystem.db")
            self.cursor = self.conn.cursor()
            self.connected = True
        except Exception as erro:
            print(sys.exc_info()[0], erro)

    def execute(self, comando: str, parms = None):
        if self.connected:
            try:
                if parms == None:
                    self.cursor.execute(comando)
                else:
                    self.cursor.execute(comando, parms)
                    return True
            except Exception as erro:
                print(sys.exc_info()[0], erro)
                return False
        
    def fetchall(self):
        return self.cursor.fetchall()
    
    def commit(self):
        self.conn.commit()

    def disconnect(self):
        self.cursor.close()
        self.conn.close()
