from flask_app import app
from flask import request, redirect, render_template
from flask_app.models import book, author

@app.route("/books")
def books():
    all_books = book.Book.get_all_books()
    return render_template("books.html", all_books = all_books)

@app.route("/book/create_book", methods=["POST"])
def create_book():
    new_book = book.Book.create_book(request.form)
    return redirect("/books")

@app.route("/book/<id>")
def book_page(id):
    data = {
        "id": id
    }
    book_selected = book.Book.book_selected(data)
    fav_authors = book.Book.select_fav_authors(data)
    all_authors = author.Author.get_all_authors()
    return render_template("book.html", book_selected = book_selected, fav_authors = fav_authors, all_authors = all_authors)

@app.route("/book/add_fav_author/<id>", methods=["POST"])
def add_fav_author(id):
    data = {
        "book_id": id,
        "author_id": request.form["author_id"]
    }
    add_fav_author = book.Book.add_fav_author(data)
    return redirect(f"/book/{id}")