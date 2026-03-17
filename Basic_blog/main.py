from flask import Flask, render_template
from post import Post

app = Flask(__name__)
blog_posts = Post()
all_posts = blog_posts.all_posts
@app.route('/blog')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:id>")
def blog_post(id):
    render_post = None
    for post in all_posts:
        if post['id'] == id:
            render_post = post
    return render_template("post.html", post=render_post)

if __name__ == "__main__":
    app.run(debug=True)
