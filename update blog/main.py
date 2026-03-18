from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access teh variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

post_data = requests.get(url="https://api.npoint.io/dd1a11db7041bf5213ea")
posts = post_data.json()
data = {}

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    global data
    if request.method == "GET":
        return render_template("contact.html", form=request.method)
    else:
        data = request.form

        # Sending Email with smtplib
        subject = f"Message from reader, {data['name']}."
        body = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        message = f"Subject: {subject}\n\n{body}"

        connection = smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT))  # type: ignore
        connection.ehlo()
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)  # type: ignore
        connection.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg=message)  # type: ignore
        return render_template("contact.html", form_method=request.method)


@app.route("/post/<int:id>")
def blog_post(id):
    render_post = None
    for post in posts:
        if post["id"] == id:
            render_post = post
    return render_template("post.html", post=render_post)


if __name__ == "__main__":
    app.run(debug=True)
