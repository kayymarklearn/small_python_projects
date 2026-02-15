# NATO Phonetic Alphabet Generator

A command-line utility that converts words into their NATO phonetic alphabet equivalents.

## Features
- CSV-based NATO alphabet database
- Word-to-phonetic conversion
- Input validation with error handling
- Recursive error handling for invalid input

## Project Structure
- `main.py` - Main application logic
- `nato_phonetic_alphabet.csv` - NATO phonetic alphabet database

## Requirements
- Python 3.x
- pandas

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Ensure nato_phonetic_alphabet.csv is in the project directory

## CSV Format
```csv
letter,code
A,Alfa
B,Bravo
C,Charlie
...
```

## Usage
```bash
python main.py
```

Follow the prompt to enter a word. The program will display the NATO phonetic code for each letter.

Example:
```
Enter a word: PYTHON
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

## Features
- Case-insensitive input (converts to uppercase)
- Error handling for non-alphabetic characters
- Recursive retry on invalid input

## Notes
- Only alphabetic characters are supported
- Non-letter characters will trigger an error message
- Input is recursively re-prompted on errors

