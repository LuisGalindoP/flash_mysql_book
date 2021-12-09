from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import favorite

class Author:
    #class attribute
    db_name = "books_schema"
    #contructor
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        return MySQLConnection(cls.db_name).query_db(query)
    
    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(author_name)s, NOW(), NOW());"
        return MySQLConnection(cls.db_name).query_db(query, data)

    @classmethod
    def select_author_by_id(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        result = MySQLConnection(cls.db_name).query_db(query, data)
        author_selected = cls(result[0])
        return author_selected

    @classmethod
    def select_fav_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE author_id = %(id)s;"
        result = MySQLConnection(cls.db_name).query_db(query, data)
        fav_books = []
        for i in result:
            this_book = favorite.Favorite(i)
            fav_books.append(this_book)
        return fav_books

    @classmethod
    def add_favorite_id(cls, data):
        query_check = "SELECT * FROM favorites WHERE book_id = %(book_id)s AND author_id = %(author_id)s;"
        check = MySQLConnection(cls.db_name).query_db(query_check, data)
        if len(check) > 0:
            return None
        else:
            query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
            result = MySQLConnection(cls.db_name).query_db(query, data)
            return result