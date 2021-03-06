#!/usr/bin/python3
"""First Task"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def task0():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def task1():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def task2(text):
    text = text.replace('_', ' ')
    return "C %s" % escape(text)


@app.route('/python', strict_slashes=False, defaults={'text': "is cool"})
@app.route('/python/(<text>)', strict_slashes=False)
def task3(text):
    text = text.replace('_', ' ')
    return "Python %s" % escape(text)


@app.route('/number/<int:n>')
def task4(n):
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
