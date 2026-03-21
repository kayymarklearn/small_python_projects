"""
Top Movies - Flask Web Application

A personal movie collection tracker and rating application that integrates with
The Movie Database (TMDB) API to fetch movie information and allows users to
rate, rank, and review their favorite movies.

Features:
- Add movies via TMDB search
- Rate and review movies
- Dynamic ranking based on user ratings
- Delete movies from collection

Dependencies:
    Flask, Flask-Bootstrap5, Flask-SQLAlchemy, Flask-WTF, SQLAlchemy, WTForms, requests
"""

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from forms import RateMovieForm, AddMovieForm
from search_movie import SearchMovie
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models using declarative style."""

    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movies(db.Model):
    """
    SQLAlchemy model representing a movie entry in the collection.

    Attributes:
        id: Unique identifier (primary key)
        title: Movie title (required, unique)
        year: Release year (required)
        description: Movie synopsis (required)
        rating: User rating from 0-10 (required)
        ranking: Dynamic rank based on rating (unique)
        review: User's personal review (required)
        img_url: TMDB poster image URL (required)
    """

    __tablename__ = "Movies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """
    Home route displaying the movie collection sorted by rating.

    Movies are dynamically re-ranked based on their rating (highest rated first).
    Rankings are recalculated on each page load.

    Returns:
        Rendered index.html template with movies sorted by rating in descending order.
    """
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    movies = result.scalars().all()

    for i, movie in enumerate(movies):
        movie.ranking = len(movies) - i

    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_rating():
    """
    Route for editing a movie's rating and review.

    Query Parameters:
        id: The ID of the movie to edit

    Methods:
        GET: Display the edit form pre-filled with current values
        POST: Process form submission and update the movie

    Returns:
        Redirect to home on success, or render edit.html with form.
    """
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_id = request.args.get("id")
        movie_to_update = db.get_or_404(Movies, movie_id)
        movie_to_update.rating = form.new_rating.data
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete_movie():
    """
    Route for deleting a movie from the collection.

    Query Parameters:
        id: The ID of the movie to delete

    Returns:
        Redirect to home page after deletion.
    """
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movies, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """
    Route for searching and adding new movies to the collection.

    Allows users to search for movies by title via TMDB API and displays
    a list of matching results for the user to select from.

    Methods:
        GET: Display the search form
        POST: Search TMDB and display results in select.html

    Returns:
        Rendered select.html with search results, or add.html with empty form.
    """
    form = AddMovieForm()
    if form.validate_on_submit():
        new_movie = SearchMovie(title=(form.movie_title.data).lower())
        all_movies = new_movie.find_movie()
        return render_template("select.html", movies=all_movies)
    return render_template("add.html", form=form)


@app.route("/get-movie-details")
def get_movie_details():
    """
    Route for retrieving detailed information about a selected movie.

    Fetches full movie details from TMDB (including poster, year, description)
    and creates a new Movies entry in the database. Then redirects to the
    edit page for the user to rate and review the movie.

    Query Parameters:
        movie_id: The TMDB movie ID to fetch details for

    Returns:
        Redirect to edit_rating page for the newly added movie.
    """
    new_id = request.args.get("movie_id")
    new_movie = SearchMovie(id=new_id)
    new_movie.find_specific_movie()

    movie_to_add = Movies(
        id=new_movie.id,
        title=new_movie.title,
        year=new_movie.year,
        description=new_movie.description,
        img_url=new_movie.img_url,
        rating=0.0,
        ranking=0,
        review="NONE",
    )

    db.session.add(movie_to_add)
    db.session.commit()
    return redirect(url_for("edit_rating", id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)
