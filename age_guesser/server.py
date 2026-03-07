from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/guess/<name>")
def guess(name):
    GENDERIZE_URL = "https://api.genderize.io/"
    AGIFY_URL = "https://api.agify.io/"
    data = {
        "name": name
    }
    age_response = requests.get(url=AGIFY_URL, params=data)
    gender_response = requests.get(url=GENDERIZE_URL, params=data)

    age = age_response.json()["age"]
    gender = gender_response.json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
