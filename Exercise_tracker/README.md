# Exercise Tracker

An exercise tracking application that uses Google's Gemini AI to parse natural language exercise logs and stores data in a Google Sheet using the Sheety API.

## Features
- Natural language exercise input parsing
- AI-powered calorie estimation
- Exercise duration parsing
- Automatic Google Sheet integration
- Structured JSON response handling

## Requirements
- Python 3.x
- requests
- python-dotenv (recommended for environment variables)

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Set up API credentials as environment variables:
   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `SHEETY_ENDPOINT`: Your Sheety API endpoint
   - `SHEETY_BEARER`: Your Sheety API bearer token

## Usage
```bash
python main.py
```

When prompted, describe your exercise in natural language:
```
Tell me which exercise you did: I ran 5 miles in 45 minutes and did 20 push-ups
```

The AI will parse this and extract:
- Exercise type
- Duration
- Estimated calories burned

## How It Works
1. User inputs exercise description
2. Gemini API parses the input and estimates calories
3. Data is formatted with current date and time
4. Results are posted to your Sheety Google Sheet
5. Confirmation of successful data submission

## Notes
- Get Gemini API key from [Google AI Studio](https://aistudio.google.com)
- Set up Google Sheet integration using [Sheety](https://sheety.co)

## License

This is a personal project for educational purposes.

