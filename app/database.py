import psycopg2
from psycopg2 import OperationalError

class Database:
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = self.connect()

    def connect(self):
        try:
            return psycopg2.connect(**self.db_config)
        except OperationalError as e:
            print(f"Error connecting to the database: {e}")
            return None

    def ensure_connection(self):
        if self.conn is None or self.conn.closed:
            print("Connection lost. Reconnecting...")
            self.conn = self.connect()

    def execute_query(self, query, params=None, fetch=False):
        self.ensure_connection()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                if fetch:
                    return cursor.fetchall()
                self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()

    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()
