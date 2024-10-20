from flask import Flask, render_template, request
from blog_data import BlogData
from send_email import SendEmail

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


@app.route("/contact.html", methods=["GET"])
def contact():
    if request.args.get("name"):
        arguments = ["name", "email", "phone", "message"]
        details = [request.args.get(argument) for argument in arguments]
        message_body = "\n".join(detail for detail in details)
        email_sent = SendEmail(message=message_body)
        email_sent.send_message()
        return render_template("contact.html", sent=True)
    else:
        return render_template("contact.html", sent=False)


@app.route("/post.html")
def post():
    post_number = int(request.args.get('blog_id'))
    return render_template("post.html", post_data=DATA[post_number - 1])


if __name__ == "__main__":
    app.run(debug=True)
