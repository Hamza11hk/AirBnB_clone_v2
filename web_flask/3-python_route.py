#!/usr/bin/python3
"""python route"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hello"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """c + value of text"""
    return f'C {text.replace("_", " ")}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """c + value of text"""
    return f'Python {text.replace("_", " ")}'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
