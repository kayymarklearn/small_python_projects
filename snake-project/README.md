# Snake Game

A classic Snake game implementation using Python's Turtle graphics library.

## Features
- Classic snake movement and growth mechanics
- Food collision detection
- Wall collision detection
- Self-collision detection
- Score tracking
- Game reset functionality

## Project Structure
- `main.py` - Main game loop and collision detection
- `snake.py` - Snake class and movement logic
- `food.py` - Food spawning class
- `scoreboard.py` - Score display and management
- `data.txt` - High score storage

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

## Game Controls
- **Up Arrow** - Move up
- **Down Arrow** - Move down
- **Left Arrow** - Move left
- **Right Arrow** - Move right

## How To Play
1. Snake starts in center of screen
2. Use arrow keys to move snake
3. Eat food pellets to grow and increase score
4. Avoid hitting walls
5. Avoid hitting your own tail
6. Game ends on collision
7. Score is recorded and game resets

## Game Mechanics
- Snake moves continuously in current direction
- Can't reverse directly (go back on itself)
- Food spawns randomly
- Each food eaten increases length by 1
- Score increases by 1 per food

## Customization
Modify in main.py:
- Screen size (600x600)
- Game speed (0.1 seconds)
- Food position

## Notes
- Game resets on collision with walls or tail
- High score persists between sessions
- Click to exit game window

## License

This is a personal project for educational purposes.

