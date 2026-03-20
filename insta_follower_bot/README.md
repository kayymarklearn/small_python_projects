# Instagram Follower Bot

Automated bot that follows Instagram users from a target account's followers.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver

## Setup

1. Install dependencies:
   ```bash
   pip install selenium
   ```

2. Set environment variables:
   ```bash
   export USERNAME="your_instagram_username"
   export PASSWORD="your_instagram_password"
   ```

## Usage

```bash
python main.py
```

## Configuration

Edit `instafollower.py` to change the target account:
```python
SIMILAR_ACCOUNT = "https://www.instagram.com/username/"
```

## Notes

- Uses Instagram login credentials from environment variables
- Adds random delays to avoid detection
- Opens Chrome in debug mode to keep browser open after execution

## License

This is a personal project for educational purposes.
