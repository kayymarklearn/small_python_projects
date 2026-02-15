# US States Guessing Game

An interactive geography game where players guess US state names on a map to learn their locations.

## Features
- Interactive US map display
- State position recognition
- Score tracking
- CSV-based state data with coordinates
- States to learn export (missed states saved to CSV)
- Input validation

## Project Structure
- `main.py` - Main game loop and state logic
- `states.py` - State class for positioning
- `scoreboard.py` - Score display
- `50_states.csv` - State data with coordinates
- `blank_states_img.gif` - US map background image

## Requirements
- Python 3.x
- turtle (built-in)
- pandas

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Ensure these files are in project directory:
   - blank_states_img.gif (US map image)
   - 50_states.csv (state data)

## Usage
```bash
python main.py
```

## CSV Format
```csv
state,x,y
Alabama,-87,39
Alaska,-152,61
...
```

The x,y coordinates are pixel positions on the map image.

## How To Play
1. A blank US map displays
2. Text prompt shows current score out of 50
3. Type state names as they appear to you
4. Correct states display on the map
5. Continue until you reach 50 or type "Exit"
6. Missed states are saved to states_to_learn.csv

## Features
- **Score Tracking**: Current correct guesses displayed
- **Export Learning**: Missed states saved for review
- **Smart Input**: Case-insensitive matching
- **Quick Exit**: Type "Exit" to quit and save progress

## Output
When you exit, `states_to_learn.csv` is created with states you missed for future study.

## Tips
- Type state names as you see them on the map
- Be careful with spelling
- Take breaks and come back to learn missed states
- Each play-through helps reinforce geography

## Notes
- Screen is 750x500 pixels
- Coordinates are specific to the provided map image
- Game doesn't end until you reach 50 or exit
- Repeat to improve your score

