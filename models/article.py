from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def title(self):
        return self._title
    
    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        author = cursor.fetchone()
        conn.close()
        return author
    
    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        author = cursor.fetchall()
        conn.close()
        return author

    def __repr__(self):
        return f'<Article {self.title}>'
