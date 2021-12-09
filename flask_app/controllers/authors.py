from flask_app import app
from flask import request, redirect, render_template
from flask_app.models import author, book

@app.route("/")
def index():
    all_authors = author.Author.get_all_authors()
    return render_template("index.html", all_authors = all_authors)

@app.route("/author/create", methods=["POST"])
def author_create():
    new_author = author.Author.create_author(request.form)
    return redirect(f"/author/{new_author}")

@app.route("/author/<id>")
def author_page(id):
    data = {
        "id": id
    }
    author_selected = author.Author.select_author_by_id(data)
    author_fav_books = author.Author.select_fav_books(data)
    all_books = book.Book.get_all_books()
    return render_template("/author.html", author_selected = author_selected, author_fav_books = author_fav_books, all_books = all_books)

@app.route("/authors/add_favorite/<id>", methods=["POST"])
def add_favorite(id):
    data = {
        "book_id":request.form["book_id"],
        "author_id": id
    }
    add_favorite_id = author.Author.add_favorite_id(data)
    return redirect(f"/author/{id}")