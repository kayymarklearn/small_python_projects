"""
WTForms form definitions for the Top Movies application.

This module defines Flask-WTF form classes used for:
- Rating and reviewing movies
- Searching for movies to add

Dependencies:
    wtforms, flask_wtf
"""

from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class RateMovieForm(FlaskForm):
    """
    Form for rating and reviewing a movie.

    Fields:
        new_rating: Float field for movie rating (0-10 scale)
        new_review: String field for user's personal review
        submit: Submit button to save changes

    Validation:
        All fields are required (DataRequired validator).
    """

    new_rating = FloatField(
        "Your Rating out of 10 e.g. 7.5", validators=[DataRequired()]
    )
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    """
    Form for searching and adding movies to the collection.

    Fields:
        movie_title: String field for movie title search query
        submit: Submit button to trigger TMDB search

    Validation:
        Movie title field is required (DataRequired validator).
    """

    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
