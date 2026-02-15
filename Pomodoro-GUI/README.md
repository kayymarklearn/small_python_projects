# Pomodoro Timer GUI

A Tkinter-based Pomodoro timer implementing the Pomodoro Technique for productivity.

## Features
- 25-minute work sessions (configurable)
- 5-minute short breaks
- 20-minute long breaks
- Visual timer display
- Session tracking with checkmarks
- Start and reset controls
- Color-coded timer labels

## Requirements
- Python 3.x
- tkinter (usually built-in)
- math (built-in)

## Installation & Setup
1. Clone or download the project
2. Ensure tomato.png image file is in the project directory
3. No external dependencies required

## Usage
```bash
python main.py
```

## How It Works
1. Click "Start" to begin a 25-minute work session
2. After work session, 5-minute short break begins
3. After 4 work sessions, a 20-minute long break begins
4. Checkmarks appear for each completed work session
5. Click "Reset" to restart the timer

## Timer Sequence
- Session 1-2: Work (25min) → Short Break (5min)
- Session 3-4: Work (25min) → Short Break (5min)
- Session 5-6: Work (25min) → Short Break (5min)
- Session 7-8: Work (25min) → Long Break (20min)
- Cycle repeats

## Customization
Modify these constants in main.py:
- `WORK_MIN = 25` - Work session duration
- `SHORT_BREAK_MIN = 5` - Short break duration
- `LONG_BREAK_MIN = 20` - Long break duration

## Notes
- Timer displays in MM:SS format
- Background image provides visual appeal
- Checkmarks indicate completed sessions
- Easy to reset and start over

