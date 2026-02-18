# Flight Club

A Python automation script that scans flight deals and notifies subscribers when prices drop below your target. It pulls destinations and prices from a Google Sheet via Sheety, uses the Amadeus API to search flights, and sends email alerts (optionally SMS/WhatsApp via Twilio).

## Features

- Auto-fills missing IATA codes in your destinations sheet.
- Searches for direct flights first, then indirect flights if no direct options exist.
- Finds the cheapest offer and alerts subscribers when the price is below your target.
- Sends email notifications to everyone in your users sheet.

## Project Structure

- `main.py`: Orchestrates the flow (sheet update, flight search, notifications).
- `data_manager.py`: Reads/writes Sheety data for destinations and users.
- `flight_search.py`: Authenticates with Amadeus and performs flight searches.
- `flight_data.py`: Normalizes and selects the cheapest flight result.
- `notification_manager.py`: Sends notifications (email, SMS, WhatsApp).

## Requirements

- Python 3.9+
- API accounts for Amadeus and Sheety
- (Optional) Twilio account for SMS/WhatsApp

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```bash
# Amadeus API
AMADEUS_API_KEY=your_amadeus_key
AMADEUS_SECRET=your_amadeus_secret

# Sheety (Google Sheets API wrapper)
SHEETY_USRERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password
SHEETY_PRICES=https://api.sheety.co/your_project/prices
SHEETY_USERS=https://api.sheety.co/your_project/users

# Email (SMTP)
EMAIL_PROVIDER_SMTP_ADDRESS=smtp.gmail.com
MY_EMAIL=your_email@example.com
MY_EMAIL_PASSWORD=your_email_password

# Twilio (optional)
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_VIRTUAL_NUMBER=+1234567890
TWILIO_VERIFIED_NUMBER=+1234567890
TWILIO_WHATSAPP_NUMBER=+14155238886
```

Notes:
- `SHEETY_USRERNAME` is spelled to match the current code.
- If you want to use SMS/WhatsApp, ensure your Twilio numbers are verified.

## Google Sheet Schema

Your prices sheet should include these columns:

- `city` (e.g., Paris)
- `iataCode` (blank to auto-fill)
- `lowestPrice` (target price threshold)
- `id` (Sheet row ID used by Sheety)

Your users sheet should include:

- `whatIsYourEmail?` (subscriber email)

## Running

```bash
python main.py
```

The script will:

1. Fetch destination data from Sheety.
2. Update missing IATA codes.
3. Search for flights for the next six months.
4. Notify subscribers when a cheaper flight is found.

## Customization

- Change the origin airport in `main.py` (`ORIGIN_CITY_IATA`).
- Adjust the date window or search parameters in `main.py` and `flight_search.py`.
- Enable SMS/WhatsApp by uncommenting the relevant lines in `main.py`.

## Troubleshooting

- If Amadeus requests fail, confirm your token and API credentials.
- If Sheety requests fail, verify endpoints and Basic Auth credentials.
- Email sending requires an SMTP provider that permits your credentials.

## License

This project is for personal/educational use. Add a license if you plan to share or distribute it.
