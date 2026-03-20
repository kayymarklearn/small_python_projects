# Kanye Quotes Generator

A GUI application built with Tkinter that fetches and displays random Kanye West quotes.

## Features
- Tkinter-based GUI interface
- Fetches random quotes from Kanye Rest API
- Error handling for failed requests
- One-click quote refresh
- Clean, minimalist design

## Requirements
- Python 3.x
- tkinter (usually built-in)
- requests
- PIL/Pillow (for image support)

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install requests pillow
   ```
3. Ensure image files are in the project directory:
   - background.png (300x414 px recommended)
   - kanye.png (button image)

## Usage
```bash
python main.py
```

## How It Works
1. Window displays background image
2. Click the Kanye button to fetch a random quote
3. Quote appears centered on the canvas
4. Error message displays if API is unreachable
5. Application continues to fetch new quotes on each click

## Features
- **Auto-fetch**: Gets a quote when the app launches
- **Error Handling**: Shows friendly message if API fails
- **Simple UI**: Minimalist design focused on the quotes

## Notes
- Quotes are fetched from https://api.kanye.rest/
- No authentication required
- Internet connection required to fetch quotes

## License

This is a personal project for educational purposes.

