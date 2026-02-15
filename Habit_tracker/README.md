# Habit Tracker

An application that tracks daily habits using the Pixela API, creating and managing a pixel graph for visualization.

## Features
- Pixela API integration for habit tracking
- Pixel graph creation and management
- User authentication using tokens
- Habit data persistence
- API endpoints for CRUD operations

## Requirements
- Python 3.x
- requests
- python-dotenv (recommended)

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Set up environment variables:
   - `USERNAME`: Your Pixela username
   - `USER_TOKEN`: Your Pixela user token
4. Get Pixela account at [pixe.la](https://pixe.la)

## Usage
Currently, this application demonstrates the Pixela API functionality. You can:
- Create a user account
- Create a graph for tracking
- Add daily pixels
- Update pixel data
- Delete pixels

## How It Works
The application uses HTTP requests to interact with Pixela's REST API:
- **POST** - Create resources (users, graphs, pixels)
- **PUT** - Update existing pixels
- **DELETE** - Remove pixels
- **GET** - Retrieve pixel data

## Notes
- Date format used: YYYYMMDD
- The code includes commented examples for each operation
- Uncomment sections to execute specific operations
- Your token must be kept secure

