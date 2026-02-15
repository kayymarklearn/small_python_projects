# Stock Trading News Alert

An application that monitors stock price changes and sends SMS alerts with related news articles.

## Features
- Stock price tracking via Alpha Vantage API
- Percentage change calculation
- News fetching from NewsAPI
- SMS alerts via Twilio
- Multiple article distribution
- Visual indicators (🔺 up, 🔻 down)

## Requirements
- Python 3.x
- requests
- newsapi
- twilio

## Installation & Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install requests newsapi twilio
   ```
3. Set up environment variables:
   - `VANTAGE_API`: Alpha Vantage API key
   - `NEWS_API`: News API key
   - `ACCOUNT_SID`: Twilio account SID
   - `AUTH_TOKEN`: Twilio auth token
   - `MESSAGING_SERVICE_SID`: Twilio messaging service SID
   - `MY_NUMBER`: Your phone number

4. Get credentials:
   - [Alpha Vantage](https://www.alphavantage.co)
   - [NewsAPI](https://newsapi.org)
   - [Twilio](https://www.twilio.com)

## Usage
```bash
python main.py
```

## How It Works
1. Fetches stock data for TSLA (Tesla)
2. Compares yesterday's close to day before
3. Calculates percentage change
4. If change ≥ 5%, fetches 3 latest news articles
5. Sends SMS with company name, percentage, headline, and brief
6. Repeats monitoring process

## Customization
Change default stock:
```python
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
```

## Message Format
```
TSLA: 🔺5%
Headline: Your article headline here
Brief: Article summary...
```

## Alert Threshold
Default: 5% price change triggers alerts
Edit `if (abs(percentage_change)) >= 5:` line

## Notes
- Checks market data once per run
- Alpha Vantage has rate limits on free tier
- SMS charges apply per Twilio plan
- Use environment variables for security

