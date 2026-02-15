# Hangman Game

A classic command-line Hangman word guessing game in Python with visual stages.

## Features
- Random word selection from word list
- Visual hangman stages display
- Terminal-based gameplay
- Letter guessing with feedback
- Game state tracking

## Project Structure
- `main.py` - Main game logic
- `hang_arts.py` - Hangman ASCII art and stages
- `hang_words.py` - Word list for game

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
1. A random word is selected
2. Guess one letter at a time
3. Correct guesses reveal letter positions
4. Incorrect guesses display hangman stages
5. Win by guessing all letters before running out of lives
6. You have 6 incorrect guesses allowed

## Game Rules
- Each wrong guess costs one life
- You start with 6 lives
- Game ends when you win or run out of lives
- One letter guess per turn

## Notes
- Word list can be customized by editing hang_words.py
- Visual stages progress from empty to complete hangman
- Case-insensitive letter matching

