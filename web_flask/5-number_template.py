#!/usr/bin/python3
""" Importing the flask module """

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ A funtion that defines a return value. """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ A funtion that defines a return value. """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ A funtion that defines a return value. """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth(text="is cool"):
    """ A funtion that defines a return value. """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_or_not(n):
    """ A funtion that checks if number or not. """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html_page(n):
    """ A funtion that checks display a page if number. """
    if isinstance(n, int):
        return render_template("5-number.html", num=n)


if __name__ == "__main__":
    app.run()
