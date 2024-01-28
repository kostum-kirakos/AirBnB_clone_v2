#!/usr/bin/python3
""" Importing the flask module """

from flask import Flask
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


if __name__ == "__main__":
    app.run()
