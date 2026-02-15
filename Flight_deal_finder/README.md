# Flight Deal Finder

A Python application that monitors flight prices and sends SMS notifications when deals are found below your target price threshold.

## Overview

Flight Deal Finder compares current flight prices against historical low prices stored in a Google Sheet. When it finds flights cheaper than your recorded lowest price, it automatically sends SMS alerts via Twilio, allowing you to book deals quickly.

## Features

- **Automatic Flight Monitoring**: Continuously searches for flights across your destination list
- **Price Comparison**: Compares current flight prices against your historical low price benchmarks
- **SMS Notifications**: Sends real-time alerts via Twilio when deals are found
- **Extended Search Range**: Searches flights up to 180 days in advance in 7-day intervals
- **City Input**: Dynamically accepts your current location as input
- **Multi-Destination Support**: Monitor multiple destination cities simultaneously

## Project Structure

```
flight_deal_finder/
├── main.py                    # Entry point - orchestrates the entire workflow
├── flight_data.py             # Structures flight data and integrates components
├── flight_search.py           # Handles Amadeus API for flight searches
├── data_manager.py            # Manages Google Sheet data via Sheety API
├── notification_manager.py    # Sends SMS notifications via Twilio
└── README.md
```

## Components

### `main.py`
The entry point that:
- Prompts for the user's current city
- Fetches flights using FlightData
- Triggers notifications for available deals

### `flight_data.py` 
Coordinates the flight search process:
- Retrieves destination list and price thresholds from Google Sheets
- Searches for flights from current location to each destination
- Filters and structures flight information
- Returns available flights below target prices

### `flight_search.py`
Integrates with the Amadeus Flight Search API:
- Authenticates and obtains access tokens
- Converts city names to IATA codes
- Searches flights with price parameters
- Returns cheapest available options

### `data_manager.py`
Manages destination and pricing data:
- Fetches flight destination list from Google Sheets via Sheety API
- Each entry contains: city name, IATA code, and lowest historical price

### `notification_manager.py`
Handles SMS notifications:
- Formats flight deal messages with price, times, and locations
- Sends SMS alerts via Twilio API
- Includes rate limiting between messages

## Requirements

### Python Package Dependencies
```
requests            # For API calls to external services
twilio              # For SMS notifications
```

### External APIs & Services

1. **Amadeus API** (Flight Search)
   - Endpoint: `https://test.api.amadeus.com/v2`
   - Used for searching flight offers

2. **Sheety API** (Google Sheets Integration)
   - Endpoint: `https://api.sheety.co`
   - Used to fetch destination cities and price thresholds

3. **Twilio API** (SMS Notifications)
   - Used to send SMS alerts to your phone

## Setup & Installation

### 1. Environment Variables

Create a `.env` file or set the following environment variables:

```bash
# Amadeus API Credentials
export AMD_KEY="your_amadeus_api_key"
export AMD_SECRET="your_amadeus_api_secret"

# Sheety API Token (for Google Sheets)
export SHEETY_BEARER="your_sheety_bearer_token"

# Twilio Credentials
export ACCOUNT_SID="your_twilio_account_sid"
export TWILIO_TOKEN="your_twilio_auth_token"
```

### 2. Install Dependencies

```bash
pip install requests twilio
```

### 3. Google Sheets Setup

Create a Google Sheet with a "prices" sheet containing:

| city       | iataCode | lowestPrice |
|-----------|----------|------------|
| Paris     | CDG      | 50         |
| Barcelona | BCN      | 45         |
| Berlin    | BER      | 40         |

Connect it to Sheety to get the API endpoint.

### 4. Twilio Setup

1. Create a Twilio account
2. Get your Account SID and Auth Token
3. Set up a phone number to send messages from
4. Update phone numbers in `notification_manager.py`:
   - `from_` field: Your Twilio phone number
   - `to` field: Your personal phone number

## Usage

Run the application:

```bash
python main.py
```

You'll be prompted to enter your current city:
```
What is your current city: LONDON
```

The application will:
1. Get your current location's IATA code
2. Search flights from your location to each destination
3. Compare prices against the lowest price targets
4. Send SMS notifications for any deals found

## Data Flow

```
User Input (Current City)
    ↓
FlightData → DataManager (fetches destinations from Google Sheets)
    ↓
FlightSearch → Amadeus API (searches flights)
    ↓
Compare prices against thresholds
    ↓
NotificationManager → Twilio API (sends SMS alerts)
```

## Example Notification

```
Low price alert! Only £30 to fly from LONDON-LHR to PARIS-CDG,
from 2026-02-20 to 2026-02-21
```

## Notes

- Searches check 180 days in advance in 7-day intervals
- Rate limiting (60 seconds between SMS messages) prevents API throttling
- Only returns the cheapest flight option for each destination
- Requires valid API credentials for all services
- Prices are compared as grand totals including taxes and fees

## Future Enhancements

- Add persistence to track historical searches
- Implement scheduling with APScheduler for periodic checks
- Email notifications as an alternative to SMS
- User preference settings for price ranges and search frequencies
- Web interface for easier configuration
- Database for storing flight deals history

## License

This is a personal project for educational purposes.
