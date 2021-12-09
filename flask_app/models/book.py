from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import favorite, author

class Book:
    #class attribute
    db_name = "books_schema"
    #contructor
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        result = MySQLConnection(cls.db_name).query_db(query)
        all_books = []
        for book in result:
            this_book = cls(book)
            all_books.append(this_book)
        return all_books

    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        return MySQLConnection(cls.db_name).query_db(query, data)

    @classmethod
    def book_selected(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s"
        result = MySQLConnection(cls.db_name).query_db(query, data)
        book_selected = cls(result[0])
        return book_selected

    @classmethod
    def select_fav_authors(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE book_id = %(id)s;"
        result = MySQLConnection(cls.db_name).query_db(query, data)
        favorite_authors = []
        for names in result:
            this_author = author.Author(names)
            favorite_authors.append(this_author)
        return favorite_authors

    @classmethod
    def add_fav_author(cls, data):
        query_check = "SELECT * FROM favorites WHERE author_id = %(author_id)s AND book_id = %(book_id)s;"
        check = MySQLConnection(cls.db_name).query_db(query_check, data)          
        if len(check) > 0:
            return None
        else:
            query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
            return MySQLConnection(cls.db_name).query_db(query, data)
            