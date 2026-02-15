# Pong Arcade Game

A classic Pong game implementation using Python's Turtle graphics library with two-player gameplay.

## Features
- Classic Pong gameplay mechanics
- Two-player controls
- Real-time ball physics
- Collision detection
- Score tracking
- Customizable game speed

## Project Structure
- `main.py` - Main game loop
- `paddle.py` - Paddle class for players
- `ball.py` - Ball movement and physics
- `scoreboard.py` - Score tracking and display

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

### Right Paddle (Player 1)
- **Up Arrow** - Move up
- **Down Arrow** - Move down

### Left Paddle (Player 2)
- **W** - Move up
- **S** - Move down

## How To Play
1. Ball starts in center
2. Players use paddles to block ball
3. If ball passes paddle, opponent scores
4. Game continues indefinitely
5. First to score wins the rally
6. Click window to exit

## Game Mechanics
- Ball bounces off top and bottom walls
- Ball bounces off paddles
- Ball speeds up slightly each rally
- Score increases on successful block

## Notes
- Game runs at smooth 60 FPS
- Paddles are 100 units tall
- Ball size auto-scales
- Screen is 800x600 pixels

