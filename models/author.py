from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        if not isinstance(name, str):
            return TypeError("Please input a name of type str.")
        if len(name) == 0:
            return ValueError("Please fill in your name.")
        
        self.id = id
        self.name = name
        
    def id(self,id):
        self.id
        
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()
        
    def magazines(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return [Magazine(magazine['id'], magazine['name'], magazine['category']) for magazine in magazines]

    @classmethod
    def create_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS authors")
        conn.commit()
        conn.close()

    @classmethod
    def all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        conn.close()
        return [cls(author['id'], author['name']) for author in authors]