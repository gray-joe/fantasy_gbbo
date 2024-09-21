class League:
    def __init__(self, db):
        self.db = db

    def create_league(self, name, code):
        query = """
        INSERT INTO leagues (name, code)
        VALUES (%s, %s) RETURNING id;
        """
        try:
            result = self.db.execute_query(query, (name, code), fetch=True)
            self.db.conn.commit()
            return result[0][0] if result else None
        except Exception as e:
            print(f"Error in create_league: {e}")
            raise

    def get_league(self, id):
        query = "SELECT * FROM leagues WHERE id = %s"
        result = self.db.execute_query(query, (id,), fetch=True)
        return result[0] if result else None

    def update_league(self, id, name=None, code=None):
        query = "UPDATE leagues SET name = %s, code = %s WHERE id = %s"
        self.db.execute_query(query, (name, code, id))

    def delete_league(self, id):
        query = "DELETE FROM leagues WHERE id = %s"
        self.db.execute_query(query, (id,))
