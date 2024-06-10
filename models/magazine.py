class Magazine:
    def __init__(self, id, name, category):
        if (2 <= len(name) <= 16):
            return ValueError("Character should be between 2 to 16")
        if not isinstance(category, str):
            return TypeError("Category should be a str.")
        if len(category) == 0:
            return ValueError("Please fill in the category.")
               
        self.id = id
        self.name = name
        self.category = category

    def id(self,id):
        self.id
    
    def name(self,name):
        self.name
        
    def category(self,category):
        self.category = category 
               
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        articles = cursor.fetchall()
        conn.close()
        return articles
    
    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        contributors = cursor.fetchall()
        conn.close()
        return contributors
    
    def articles_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        articles_titles = cursor.fetchall()
        conn.close()
        return [title[0] for title in articles_titles]if articles_titles else None
    
    def contributors_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        contributing_authors = cursor.fetchall()
        conn.close()
        return [author[0] for author in contributing_authors]if contributing_authors else None    
    
    
    def __repr__(self):
        return f'<Magazine {self.name}>'
