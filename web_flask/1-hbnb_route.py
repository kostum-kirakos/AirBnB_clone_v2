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


if __name__ == "__main__":
    app.run()
