# ISS Overhead Notifier

An application that sends you an email notification when the International Space Station (ISS) is passing overhead at night.

## Features
- ISS location tracking via Open Notify API
- Sunset/sunrise calculations for your location
- Email notifications when ISS passes overhead
- Location-based distance check (±5 degrees)
- Night-time check to avoid daytime alerts

## Requirements
- Python 3.x
- requests
- smtplib (built-in)

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Configure your location and email:
   - `MY_LAT` & `MY_LONG`: Your latitude and longitude
   - `MY_EMAIL`: Your Gmail address
   - `MY_PASSWORD` environment variable: Gmail app-specific password

## Usage
```bash
python main.py
```

## How It Works
1. Fetches current ISS position from Open Notify API
2. Compares with your location (within ±5 degrees)
3. Gets local sunrise/sunset times from Sunrise-Sunset API
4. Checks if it's currently nighttime
5. Sends an email if ISS is nearby and it's dark
6. Can be scheduled to run periodically (every 60 seconds)

## Coordinates
Some example coordinates:
- London: 51.5074° N, 0.1278° W
- New York: 40.7128° N, 74.0060° W
- Tokyo: 35.6762° N, 139.6503° E

## Notes
- For Gmail, use an App Password (not your regular password)
- Add `time.sleep(60)` and loop to check every 60 seconds
- The "Look Up 👆" emoji makes it easy to spot in inbox

## License

This is a personal project for educational purposes.

