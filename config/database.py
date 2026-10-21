
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.db_name = 'perpustakaan'
        self.username = "root"
        self.password = ""
        self.conn = None
        
    def get_connection(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.db_name,
                user=self.username,
                password=self.password
            )
            if self.conn.is_connected():
                return self.conn
        except Error as e:
            print(f"Koneksi Gagal: {e}")
            return None
