# Turtle Crossing Game

An interactive game where a turtle must cross a busy street while avoiding oncoming cars.

## Features
- Progressive difficulty (cars move faster each level)
- Collision detection
- Level tracking and advancement
- Car generation and movement
- Player movement controls
- Game over detection

## Project Structure
- `main.py` - Main game loop and collision logic
- `player.py` - Player turtle class
- `car_manager.py` - Car generation and movement
- `scoreboard.py` - Level display and game over screen

## Requirements
- Python 3.x
- turtle (built-in)

## Installation & Setup
1. Clone or download the project
2. No external dependencies required

## Usage
```bash
python main.py
```

## How To Play
1. Turtle starts at bottom of screen
2. Press **Up Arrow** to move up
3. Avoid oncoming cars
4. Reach the top to advance to next level
5. Each level increases car speed
6. Game over if hit by car

## Game Mechanics
- Cars spawn randomly and move left
- Difficulty increases per level
- Player has collision detection
- Goal is at top of screen
- Once player reaches top, level increases

## Controls
- **Up Arrow** - Move turtle up
- **Click to exit** - Close window

## Levels
- **Level 1**: Cars at normal speed
- **Level 2**: Cars faster
- **Level 3+**: Progressively faster cars

## Notes
- Screen is 600x600 pixels
- Cars spawn at random heights
- Car speed increases by 10 units per level
- Smooth scrolling animation

