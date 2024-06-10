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
        
    def name(self,name):
        self.name
        
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        articles = cursor.fetchall()
        conn.close()
        return articles
    
    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        magazines = cursor.fetchall()
        conn.close()
        return magazines

    def __repr__(self):
        return f'<Author {self.name}>'
