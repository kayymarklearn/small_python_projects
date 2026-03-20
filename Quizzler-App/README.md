# Quizzler GUI Quiz App

A GUI-based trivia quiz application using Tkinter with questions fetched from the Open Trivia Database.

## Features
- Multiple-choice quiz interface
- TrIvia questions fetched from Open Trivia Database
- Score tracking with visual feedback
- HTML entity parsing for special characters
- True/False question format
- Progress indication

## Project Structure
- `main.py` - Application entry point
- `ui.py` - Tkinter GUI interface
- `quiz_brain.py` - Quiz logic
- `question_model.py` - Question class
- `data.py` - Data fetching from API

## Requirements
- Python 3.x
- tkinter (usually built-in)
- requests

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. No external configuration needed

## Usage
```bash
python main.py
```

## How To Play
1. Application window opens with a question
2. Click **True** or **False** button to answer
3. Immediate feedback: green (correct) or red (incorrect)
4. Score updates at top of window
5. Next question appears after feedback
6. Final score shown when quiz ends

## Features
- **10 Questions** by default (customizable)
- **HTML Parsing** - Handles special characters
- **Score Display** - Shows current progress
- **Immediate Feedback** - Color-coded responses
- **Clean UI** - Simple and intuitive

## Customization
Edit data.py to change:
- Number of questions
- Question categories
- Difficulty level

## Notes
- Questions sourced from Open Trivia Database API
- Internet connection required
- Randomized question selection

## License

This is a personal project for educational purposes.

