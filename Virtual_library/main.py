from flask import Flask, render_template, request, redirect, url_for
from enum import auto, unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import url
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# Create the database
class Base(DeclarativeBase):
    pass


# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Crate the extension
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    # This will set the table name, default is python will use the class name in snake_case
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed
    def __repr__(self):
        return f"<Book {self.title}>"


# Create table schema in the database. Requires application context
with app.app_context():
    db.create_all()

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""


all_books = []


@app.route("/")
def home():

    books = db.session.execute(db.select(Books).order_by(Books.id))
    all_books = books.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Books(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"]),
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        book_id = request.form.get("id")
        book_id = int(book_id)
        updated_book = db.get_or_404(Books, book_id)
        updated_book.rating = request.form.get("new_rating")
        db.session.commit()
        return redirect(url_for("home"))
    else:
        book = db.session.execute(
            db.select(Books).where(Books.id == int(request.args.get("id")))
        ).scalar()
        return render_template("edit.html", book=book)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book = db.get_or_404(Books, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
