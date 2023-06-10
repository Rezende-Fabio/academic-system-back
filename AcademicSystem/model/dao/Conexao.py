import sqlite3

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
        except:
            print("E")

    def execute(self, comando: str):
        if self.connected:
            try:
                self.conn.execute(comando)
                return True
            except:
                return False
        
    def fetchall(self):
        return self.cursor.fetchall()
    
    def commit(self):
        self.conn.commit()

    def disconnect(self):
        self.cursor.close()
        self.conn.close()
