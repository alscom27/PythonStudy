from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s!" % name


@app.route("/flask")
def hello_flask():
    return "Hello Flask"


@app.route("/python/")
def hello_python():
    return "Hello python"


@app.route("/admin")
def hello_admin():
    return "Hello Admin"


@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"Hello {guest} as Guest"


@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))


if __name__ == "__main__":
    app.run(debug=True)
