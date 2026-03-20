# Automated Birthday Wisher

A Python application that automatically sends personalized birthday emails to contacts on their special day.

## Features
- Reads birthday dates from a CSV file
- Sends personalized birthday emails using Gmail SMTP
- Randomly selects from multiple birthday message templates
- Email templating with name replacement
- Secure credential management using environment variables

## Project Structure
- `main.py` - Main application logic
- `birthdays.csv` - Data file with contact information (name, email, month, day)
- `letter_templates/` - Folder containing birthday message templates (letter_1.txt, letter_2.txt, letter_3.txt)

## Requirements
- Python 3.x
- pandas
- smtplib (built-in)

## Installation & Setup

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Create a `birthdays.csv` file with the following format:
   ```csv
   name,email,month,day
   Alice,alice@example.com,8,15
   Bob,bob@example.com,3,22
   ```
4. Create `letter_templates/` directory and add template files (letter_1.txt, letter_2.txt, letter_3.txt)
5. Set up environment variables:
   - `MY_GMAIL_PASSWORD`: Your Gmail app-specific password

## Usage
```bash
python main.py
```

The script automatically checks if today is anyone's birthday and sends an email if a match is found.

## Notes
- For Gmail, you'll need to use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password
- Gmail SMTP server: smtp.gmail.com (port 587)
- The script runs once; for automated daily execution, consider using a scheduler (cron, Task Scheduler, etc.)

## License

This is a personal project for educational purposes.

