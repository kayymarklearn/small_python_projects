# Hirst Color Art Generator

A Python script that generates dot pattern art using the Turtle graphics library, inspired by Damien Hirst's pointillist artwork.

## Features
- Generates 10x10 grid of colored dots
- Uses pre-defined color palette (15 colors)
- Turtle graphics-based drawing
- Fast rendering with optimized turtle settings

## Requirements
- Python 3.x
- turtle (built-in)
- colorgram.py (optional - for extracting colors from images)

## Installation & Setup
1. Clone or download the project
2. No external dependencies required for basic usage

## Usage
```bash
python main.py
```

### Optional: Extract Colors from Image
To use custom colors from an image, install colorgram:
```bash
pip install colorgram.py
```

Then uncomment the color extraction code in main.py and provide an image file.

## How It Works
1. Creates a turtle and sets up the screen
2. Positions the turtle at the starting point
3. Draws a 10x10 grid of dots
4. Each dot is colored randomly from the palette
5. Automatically closes when you click the window

## Color Palette
The default palette includes 15 earth-tone and rich colors that can be customized.

## Notes
- Turtle is hidden for cleaner aesthetics
- Uses fastest speed for quick rendering
- Click to exit the window

## License

This is a personal project for educational purposes.

