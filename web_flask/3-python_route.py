#!/usr/bin/python3
"""Add defaults if params are not present."""


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


@app.route('/c/<string:text>')
def handle_params(text):
    """Handle parameters passed in the URL."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/<string:text>')
@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
def handle_defaults(text):
    """Put a default value if params are not passed."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
