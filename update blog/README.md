# Update Blog

A Flask-based blog application that displays posts fetched from an API, with a contact form that sends emails via SMTP.

## Features

- Blog post display from external API
- Individual post pages
- About page
- Contact form with email functionality via SMTP
- Responsive HTML templates using Jinja2

## Project Structure

- `main.py` - Flask application with routes
- `templates/` - HTML templates for pages
- `.env` - Environment variables (SMTP configuration)

## Requirements

- Python 3.x
- Flask
- requests
- python-dotenv

## Installation & Setup

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install flask requests python-dotenv
   ```
3. Set up environment variables in `.env`:
   - `SMTP_SERVER` - Your SMTP server (e.g., smtp.gmail.com)
   - `SMTP_PORT` - SMTP port (e.g., 587 for TLS)
   - `USERNAME` - Your email address
   - `PASSWORD` - Your email password or app password

## Usage

```bash
python main.py
```

Visit `http://127.0.0.1:5000` in your browser.

### Pages

- `/` - Home page displaying all blog posts
- `/about` - About page
- `/contact` - Contact form (sends email on submission)
- `/post/<id>` - Individual blog post page

## Notes

- Posts are fetched from an external API at runtime
- Contact form submissions are sent via SMTP to the configured email address
- Update the `.env` file with your own SMTP credentials before using the contact form
