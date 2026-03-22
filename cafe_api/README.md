# Cafe API

A REST API for cafe information with SQLite database.

## Features
- Get random, all, or location-filtered cafes
- Add, update, and delete cafes
- SQLite persistence

## Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Endpoints
| Route | Method | Description |
|-------|--------|-------------|
| `/random` | GET | Get random cafe |
| `/all` | GET | Get all cafes |
| `/search?loc=<location>` | GET | Search cafes by location |
| `/add` | POST | Add new cafe |
| `/update-price/<id>?new_price=<price>` | PATCH | Update cafe price |
| `/report-closed/<id>?api-key=<key>` | DELETE | Delete cafe |
| `/documentation` | GET | API documentation |

## License

Personal project for educational purposes.
