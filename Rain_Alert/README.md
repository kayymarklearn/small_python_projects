# Rain Alert Notifier

An application that checks weather forecasts and sends SMS alerts when rain is expected.

## Features
- Weather API integration (OpenWeatherMap)
- SMS notifications via Twilio
- Forecast checking (12-hour span)
- Automatic rain detection
- SMS delivery confirmation

## Requirements
- Python 3.x
- requests
- twilio

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install requests twilio
   ```
3. Set up environment variables:
   - `API_KEY`: OpenWeatherMap API key
   - `ACCOUNT_SID`: Twilio account SID
   - `AUTH_TOKEN`: Twilio auth token
   - `TWILIO_NUMBER`: Twilio phone number
   - `MY_NUMBER`: Your phone number

4. Get credentials:
   - [OpenWeatherMap](https://openweathermap.org/api)
   - [Twilio](https://www.twilio.com)

## Usage
```bash
python main.py
```

## How It Works
1. Checks weather forecast for your location
2. Scans for rain in next 12 hours
3. If rain detected, sends SMS alert
4. Message includes reminder to bring umbrella
5. Runs once; schedule for periodic checks

## Weather Conditions
Rain is detected when weather ID is < 700 (includes):
- Thunderstorms
- Drizzle
- Rain
- Snow (treated as precipitation)

## Configuration
Customize location by editing:
- `lat` parameter (latitude)
- `lon` parameter (longitude)

Example: London (51.5074, -0.1278)

## Notes
- Works with any location using latitude/longitude
- SMS charges apply based on Twilio plan
- Use environment variables for security

## License

This is a personal project for educational purposes.

