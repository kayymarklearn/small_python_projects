from flask import Flask, render_template
import requests

post_data = requests.get(url="https://api.npoint.io/dd1a11db7041bf5213ea")
posts = post_data.json()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:id>")
def blog_post(id):
    render_post = None
    for post in posts:
        if post["id"] == id:
            render_post = post
    return render_template("post.html", post=render_post)


if __name__ == "__main__":
    app.run(debug=True)
