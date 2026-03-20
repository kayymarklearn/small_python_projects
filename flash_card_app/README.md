# Flash Card Learning App

A GUI-based flashcard application for learning French vocabulary using Tkinter. Cards automatically flip after 3 seconds.

## Features
- French-English flashcard system
- Automatic 3-second card flip timer
- Progress tracking (words to learn)
- Visual feedback with card images
- CSV-based word data management
- Persistent learning progress

## Project Structure
- `main.py` - Main application with GUI
- `data/french_words.csv` - French vocabulary data
- `data/words_to_learn.csv` - Tracks remaining words (auto-generated)
- `images/card_front.png` - Front card image
- `images/card_back.png` - Back card image

## Requirements
- Python 3.x
- tkinter (usually built-in)
- pandas

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Ensure image files are in the `images/` directory:
   - card_front.png
   - card_back.png
4. Ensure data files exist in `data/` directory:
   - french_words.csv (format: French,English)

## Usage
```bash
python main.py
```

### How To Use
1. French words appear on screen (front of card)
2. After 3 seconds, cards flip to show English translation
3. Click **✓** (checkmark) to mark word as known
4. Click **✗** (cross) to see another word
5. Progress is saved - next time you run the app, only unknown words appear

## CSV Format
`data/french_words.csv`:
```csv
French,English
Bonjour,Hello
Chat,Cat
```

## Notes
- Timer resets with each new card
- Words marked as known are removed from words_to_learn.csv
- To restart, delete words_to_learn.csv and it will regenerate from french_words.csv

## License

This is a personal project for educational purposes.

