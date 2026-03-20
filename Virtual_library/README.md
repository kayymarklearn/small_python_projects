# Virtual Library

A web application for managing your personal book collection with ratings, built with Flask and SQLAlchemy.

## Features
- Add new books with title, author, and rating
- View all books in your collection
- Edit book ratings
- Delete books from the collection
- Persistent storage using SQLite

## Project Structure
- `main.py` - Flask application with routes and database models
- `templates/` - HTML templates for the web interface
  - `index.html` - Home page displaying book list
  - `add.html` - Form to add new books
  - `edit.html` - Form to edit book ratings
- `instance/` - SQLite database storage

## Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
```bash
pip install flask flask-sqlalchemy
```

## Usage
```bash
python main.py
```

Navigate to `http://127.0.0.1:5000` in your browser.

### Routes
- `/` - View all books
- `/add` - Add a new book (GET/POST)
- `/edit` - Edit a book's rating
- `/delete` - Remove a book from the collection

## How It Works
The application uses SQLAlchemy ORM to manage a SQLite database. Each book entry contains a title, author, and rating (0-10). The Flask server handles CRUD operations through its routing system.

## License

This is a personal project for educational purposes.
