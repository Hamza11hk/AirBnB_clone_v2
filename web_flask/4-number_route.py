#!/usr/bin/python3
"""1-hbnb"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def function():
    """function"""
    return "¡Hello HBNB!"


@app.route("/hbnb")
def function2():
    """function2"""
    return "HBNB"


@app.route("/c/<text>")
def function3(text):
    """function2"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/<text>")
def function4(text):
    """function2"""
    if text is None:
        return "Python is cool"
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def function_new(n):
    """function2"""
    return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
