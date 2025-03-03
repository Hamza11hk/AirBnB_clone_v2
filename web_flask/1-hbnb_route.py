#!/usr/bin/python3
"""1-hbnb"""

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
