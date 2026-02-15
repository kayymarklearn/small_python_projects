# Etch-A-Sketch Drawing App

An interactive drawing application using Python's Turtle graphics library, allowing users to draw on screen with keyboard controls.

## Features
- Real-time drawing with turtle graphics
- Keyboard controls for movement and rotation
- Screen clearing functionality
- Home button to reset position

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

### Controls
- **W** - Move forward
- **S** - Move backward
- **D** - Turn clockwise (right)
- **A** - Turn counter-clockwise (left)
- **C** - Clear screen and reset position
- **Click to exit** - Close the window

## How It Works
The turtle moves with a 10-unit step size and rotates 10 degrees for each turn command. The screen clears by lifting the pen, moving to home position, and lowering the pen again.

