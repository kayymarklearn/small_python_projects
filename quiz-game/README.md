# Quiz Game

A command-line trivia quiz game with multiple-choice questions and score tracking.

## Features
- Multiple-choice question format
- Score tracking and percentage
- Question progression
- Interactive gameplay

## Project Structure
- `main.py` - Main game loop
- `question_model.py` - Question class
- `data.py` - Question database
- `quiz_brain.py` - Quiz logic and scoring

## Requirements
- Python 3.x

## Installation & Setup
1. Clone or download the project
2. No external dependencies required

## Usage
```bash
python main.py
```

## How To Play
1. Questions appear one at a time
2. Enter your answer (True/False format)
3. Immediate feedback on correctness
4. Final score displayed at end
5. Percentage score calculated

## Question Format
Questions can be formatted in the data.py:
```python
question_data = [
    {"text": "Question text here?", "answer": "True"},
    {"text": "Another question?", "answer": "False"},
]
```

## Notes
- Case-insensitive input
- Score updates after each question
- Final statistics provided at game end

## License

This is a personal project for educational purposes.

