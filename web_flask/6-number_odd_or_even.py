#!/usr/bin/python3
"""numbeer odd or even"""
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """is n integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """html if n is integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even_n(n):
    """ odd or even"""
    odd_even = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, n_type=odd_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
