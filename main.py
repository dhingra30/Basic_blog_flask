from flask import Flask, render_template, request
from blog_data import BlogData

data = BlogData()
DATA = data.blog_data

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home_page(blog_data=DATA):
    return render_template("index.html", blog_data=blog_data)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/post.html")
def post():
    post_number = int(request.args.get('blog_id'))
    return render_template("post.html", post_data=DATA[post_number-1])


if __name__ == "__main__":
    app.run(debug=True)
