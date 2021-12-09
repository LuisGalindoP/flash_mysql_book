from flask_app.config.mysqlconnection import MySQLConnection

class Favorite:
    #class attribute
    db_name = "books_schema"
    #contructor
    def __init__(self, data):
        self.id = data["favorites.id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
