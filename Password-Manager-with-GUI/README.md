# Password Manager with GUI

A secure local password manager with a Tkinter GUI that generates strong passwords and stores them in a JSON file.

## Features
- Password generation with customizable complexity
- Secure JSON-based storage
- Search and retrieve saved passwords
- Clipboard integration for easy password copying
- User-friendly graphical interface
- Password strength with mixed case, numbers, and symbols

## Requirements
- Python 3.x
- tkinter (usually built-in)
- pyperclip

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install pyperclip
   ```
3. Ensure logo.png image file is in the project directory

## Usage
```bash
python main.py
```

## How To Use

### Generate a Password
1. Click "Generate Password"
2. A strong password is created and copied to clipboard automatically
3. Password appears in the password field

### Save a Password
1. Enter website name, email, and password
2. Click "Save"
3. Password is stored in data.json

### Search for a Password
1. Enter website name
2. Click "Search"
3. Email and password for that site are displayed

## Password Generation
- 8-10 random letters (mixed case)
- 2-4 random symbols
- 2-4 random numbers
- All shuffled together for variety

## Data Storage
Passwords are stored in `data.json`:
```json
{
    "gmail.com": {
        "email": "user@example.com",
        "password": "A1b2C3d4!@"
    }
}
```

## Security Notes
- Passwords stored locally in data.json
- No encryption - keep data.json file secure
- Use unique passwords from this manager
- Do not commit data.json to version control

