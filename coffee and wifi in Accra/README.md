# Coffee and Wifi in Accra

A Flask web application for discovering cafes in Accra, Ghana with ratings for coffee quality, wifi strength, and power socket availability.

## Overview

Coffee and Wifi in Accra helps digital nomads, remote workers, and coffee lovers find the perfect spot to work or relax. Each cafe is rated on three key factors: how good the coffee is, how strong the wifi is, and whether there are power outlets available.

## Features

- **Cafe Directory**: Browse a curated list of cafes in Accra with detailed information
- **Coffee Ratings**: Rate coffee quality on a 1-5 scale using emoji indicators
- **Wifi Strength**: Check wifi availability and strength ratings
- **Power Outlets**: See how many power sockets are available
- **Add New Cafes**: Submit new cafes to the directory via a form
- **Google Maps Integration**: Direct links to each cafe's location

## Project Structure

```
coffee and wifi in Accra/
├── main.py                    # Flask application entry point
├── forms.py                   # WTForms for cafe submission
├── cafe-data.csv              # CSV file storing cafe information
├── static/                    # Static assets
├── templates/                 # HTML templates
│   ├── base.html              # Base template with Bootstrap
│   ├── index.html             # Landing page
│   ├── add.html               # Cafe submission form
│   └── cafes.html             # Cafe listing table
├── requirements.txt           # Python dependencies
└── README.md
```

## Components

### `main.py`
The Flask application that:
- Serves the landing page at `/`
- Displays cafe listings at `/cafes` from CSV data
- Handles cafe submissions at `/add` via POST form

### `forms.py`
Defines the `CafeForm` using WTForms with:
- Cafe name (required text field)
- Google Maps URL (required with URL validation)
- Opening and closing times (required text fields)
- Coffee rating (1-5 scale with coffee cup emojis)
- Wifi strength (0-5 scale with muscle arm emojis)
- Power socket availability (0-5 scale with plug emojis)

### `cafe-data.csv`
Stores cafe information with columns:
- Cafe Name
- Location (Google Maps URL)
- Open time
- Close time
- Coffee rating
- Wifi rating
- Power rating

## Requirements

### Python Package Dependencies
```
flask                 # Web framework
flask-bootstrap5      # Bootstrap 5 integration
flask-wtf             # WTForms integration
wtforms               # Form handling
email-validator       # Email validation for forms
```

## Setup & Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python main.py
```

The application will start on `http://127.0.0.1:5000/`

## Usage

### Browse Cafes
Visit the home page and click "Show Me!" to view all listed cafes in a table format with ratings for coffee, wifi, and power.

### Add a Cafe
Navigate to `/add` to submit a new cafe. Fill in:
- Cafe name
- Google Maps location URL
- Opening and closing times
- Coffee rating (1-5)
- Wifi strength (0-5)
- Power socket availability (0-5)

### View on Google Maps
Click any "Maps Link" in the cafes table to open the cafe's location in Google Maps.

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Landing page |
| `/cafes` | GET | Display all cafes in a table |
| `/add` | GET, POST | Form to add new cafe |

## Data Storage

Cafe data is stored in `cafe-data.csv`. Each row contains:
```
Cafe Name,Location URL,Open Time,Close Time,Coffee Rating,Wifi Rating,Power Rating
```

Example entries:
```
vida e caffè,https://maps.app.goo.gl/...,6AM,9PM,☕️☕️☕️,💪💪💪💪,🔌🔌🔌🔌🔌
Koffee Lounge,https://maps.app.goo.gl/...,8AM,9PM,☕️☕️☕️,💪💪💪💪,🔌🔌🔌
```

## Rating System

### Coffee Rating
| Rating | Emoji | Meaning |
|--------|-------|---------|
| 1 | ☕️ | Poor |
| 2 | ☕️☕️ | Fair |
| 3 | ☕️☕️☕️ | Good |
| 4 | ☕️☕️☕️☕️ | Very Good |
| 5 | ☕️☕️☕️☕️☕️ | Excellent |

### Wifi Rating
| Rating | Emoji | Meaning |
|--------|-------|---------|
| 0 | ✘ | No wifi |
| 1 | 💪 | Weak |
| 2 | 💪💪 | Fair |
| 3 | 💪💪💪 | Good |
| 4 | 💪💪💪💪 | Strong |
| 5 | 💪💪💪💪💪 | Excellent |

### Power Rating
| Rating | Emoji | Meaning |
|--------|-------|---------|
| 0 | ✘ | No outlets |
| 1 | 🔌 | Few outlets |
| 2 | 🔌🔌 | Some outlets |
| 3 | 🔌🔌🔌 | Adequate |
| 4 | 🔌🔌🔌🔌 | Many outlets |
| 5 | 🔌🔌🔌🔌🔌 | Plenty of outlets |

## Notes

- The application uses Flask debug mode for development
- Data persists in `cafe-data.csv` between sessions
- Form validation ensures all fields are properly filled
- URL fields are validated to ensure valid URLs are entered

## Future Enhancements

- Add search and filter functionality
- Implement user reviews and comments
- Add cafe photos and amenities
- Include average price range for items
- Add distance from user functionality
- Implement cafe favorites/saved list
- Add map view showing cafe locations
- Export/import cafe data

## License

This is a personal project for educational purposes.
