"""
TMDB API integration for movie searching.

This module provides the SearchMovie class for interacting with The Movie Database
(TMDB) API to search for movies and retrieve detailed information including
titles, descriptions, release years, and poster images.

Dependencies:
    requests, python-dotenv
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

MOVIEDB_API_KEY = os.getenv("MOVIEDB_API_KEY")
MOVIEDB_URL = "https://api.themoviedb.org/3/search/movie"
MOVIESEARCH_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


class SearchMovie:
    """
    Client for TMDB movie search and details API.

    This class provides methods to:
    - Search for movies by title
    - Retrieve detailed information about a specific movie

    Attributes:
        title: Movie title for search queries (set on initialization)
        id: TMDB movie ID for detailed lookups (set on initialization)
        headers: HTTP headers including Bearer token for API auth
        description: Movie synopsis (populated after find_specific_movie)
        img_url: Full URL to movie poster image (populated after find_specific_movie)
        year: Movie release year as string (populated after find_specific_movie)
        all_movies: List of search results (populated after find_movie)

    Example:
        >>> search = SearchMovie(title="inception")
        >>> results = search.find_movie()
        >>> print(results[0]['title'])
        'Inception'
    """

    def __init__(self, title=None, id=None) -> None:
        """
        Initialize a SearchMovie instance.

        Args:
            title: Movie title to search for (mutually exclusive with id)
            id: TMDB movie ID for detailed lookup (mutually exclusive with title)
        """
        self.title = title
        self.id = int(id) if id is not None else None
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {MOVIEDB_API_KEY}",
        }
        self.description = ""
        self.img_url = ""
        self.year = ""

    def find_movie(self):
        """
        Search for movies by title using TMDB search endpoint.

        Makes a GET request to TMDB search/movie API and returns a list
        of matching movies with basic info (title, release date, overview, etc.).

        Returns:
            list: List of movie dictionaries from TMDB API response.
                  Each dict contains keys like 'title', 'release_date',
                  'overview', 'poster_path', 'id', etc.

        Example return structure:
            [
                {
                    'id': 27205,
                    'title': 'Inception',
                    'release_date': '2010-07-15',
                    'overview': 'A thief who steals corporate secrets...',
                    'poster_path': '/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg'
                },
                ...
            ]
        """
        params = {"query": f"{self.title}", "language": "en-US"}
        response = requests.get(url=MOVIEDB_URL, headers=self.headers, params=params)
        movie_data = response.json()
        self.all_movies = [movie for movie in movie_data["results"]]
        return self.all_movies

    def find_specific_movie(self):
        """
        Fetch detailed information for a specific movie by ID.

        Makes a GET request to TMDB movie details endpoint and populates
        instance attributes with the movie's title, poster URL, release year,
        and description/overview.

        Note:
            Requires self.id to be set (passed during initialization).

        Attributes Updated:
            self.title: Movie's original title
            self.img_url: Full URL to poster image (500px width)
            self.year: Release year extracted from release_date
            self.description: Movie synopsis/overview
        """
        response = requests.get(url=f"{MOVIESEARCH_URL}{self.id}", headers=self.headers)

        movie_data = response.json()
        self.title = movie_data["original_title"]
        self.img_url = f"{MOVIE_DB_IMAGE_URL}{movie_data['poster_path']}"
        self.year = movie_data["release_date"][:4]
        self.description = movie_data["overview"]
