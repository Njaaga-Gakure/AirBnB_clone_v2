#!/usr/bin/python3
"""Handle '/hbnb' route."""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Handle '/' route."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Handle '/hbnb' route."""
    return "HBNB"


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
