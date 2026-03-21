# Top Movies

A Flask web application for tracking, rating, and ranking your personal movie collection. Search movies via The Movie Database (TMDB) API, add them to your collection, and rate them to see dynamic rankings.

## Features

- **TMDB Integration**: Search and add movies directly from The Movie Database
- **Movie Details**: Automatically fetches titles, release years, descriptions, and poster images
- **Personal Ratings**: Rate movies on a 0-10 scale with custom reviews
- **Dynamic Ranking**: Movies are automatically re-ranked based on user ratings
- **CRUD Operations**: Add, view, edit, and delete movies from your collection
- **SQLite Database**: Persistent local storage for your movie collection

## Project Structure

```
top_movies/
├── main.py              # Flask app entry point, routes, and database models
├── forms.py             # WTForms form definitions
├── search_movie.py      # TMDB API integration
├── templates/           # HTML templates (Jinja2)
├── static/              # CSS and static assets
├── instance/            # SQLite database storage
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API keys)
└── README.md
```

## Components

### `main.py`
Flask application core:
- Flask app initialization with Bootstrap5 UI framework
- SQLAlchemy database models (Movies table)
- Route handlers for all CRUD operations

### `forms.py`
WTForms form definitions:
- `RateMovieForm`: Form for rating (0-10) and reviewing movies
- `AddMovieForm`: Form for searching movies by title

### `search_movie.py`
TMDB API client:
- `SearchMovie` class for movie search and details retrieval
- Bearer token authentication with TMDB API
- Poster image URL generation

## Requirements

- Python 3.13+
- Flask 3.1.3
- Flask-Bootstrap5
- Flask-SQLAlchemy
- Flask-WTF
- SQLAlchemy 2.0
- WTForms 3.2
- requests

## Installation & Setup

### 1. Clone or download the project

```bash
git clone <repository-url>
cd top_movies
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or using uv:

```bash
uv sync
```

### 3. Set up environment variables

Create a `.env` file with the following variables:

```bash
# Flask secret key for session security
SECRET_KEY="your-flask-secret-key"

# TMDB API Bearer Token
# Get yours at: https://www.themoviedb.org/settings/api
MOVIEDB_API_KEY="your-tmdb-bearer-token"
```

### 4. Initialize the database

The SQLite database (`movies.db`) is automatically created on first run.

```bash
python main.py
```

## Usage

### Start the Flask development server

```bash
python main.py
```

The app will be available at `http://127.0.0.1:5000/`

### Adding a Movie

1. Click "Add" on the home page
2. Enter a movie title and submit
3. Select the correct movie from search results
4. Rate the movie (0-10) and write a review
5. Click "Done" to save

### Editing Ratings

1. Click "Edit" on any movie card
2. Update the rating and/or review
3. Click "Done" to save changes

### Deleting Movies

Click "Delete" on any movie card to remove it from your collection.

## API Integration

### The Movie Database (TMDB)

This project uses TMDB API endpoints:

- **Search Movies**: `GET https://api.themoviedb.org/3/search/movie`
- **Movie Details**: `GET https://api.themoviedb.org/3/movie/{movie_id}`
- **Poster Images**: `https://image.tmdb.org/t/p/w500{poster_path}`

To obtain an API key:
1. Create a TMDB account at https://www.themoviedb.org
2. Go to Settings > API
3. Generate a new API key (select "Developer" option)
4. Use the "API Bearer Token" for authentication

## Database Schema

### Movies Table

| Column      | Type    | Constraints           |
|-------------|---------|----------------------|
| id          | INTEGER | PRIMARY KEY          |
| title       | VARCHAR | NOT NULL, UNIQUE     |
| year        | INTEGER | NOT NULL             |
| description | VARCHAR | NOT NULL             |
| rating      | FLOAT   | NOT NULL             |
| ranking     | INTEGER | NOT NULL, UNIQUE     |
| review      | VARCHAR | NOT NULL             |
| img_url     | VARCHAR | NOT NULL             |

## Routes

| Route              | Methods   | Description                           |
|-------------------|-----------|---------------------------------------|
| `/`               | GET       | Display movie collection (sorted by rating) |
| `/add`            | GET, POST | Search and add new movies             |
| `/get-movie-details` | GET    | Fetch TMDB details and create movie  |
| `/edit`           | GET, POST | Edit movie rating and review          |
| `/delete`         | GET       | Delete a movie from collection        |

## Customization

### Database Location

The database is stored at `instance/movies.db`. To change the location:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///path/to/your/db.db"
```

### Styling

Edit files in the `static/` directory for custom CSS. Bootstrap5 templates can be customized in the `templates/` folder.

## Notes

- Movie rankings are recalculated dynamically on each page load based on ratings
- The app uses debug mode by default (`app.run(debug=True)`) - disable for production
- TMDB API has rate limits; avoid excessive searches
- Poster images are served directly from TMDB's CDN

## License

This is a personal project for educational purposes.
