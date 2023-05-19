#!/usr/bin/python3
"""Route handler that handles '/' route."""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Handle the route '/' by displaying 'Hello HBNB!'."""
    return "Hello HBNB!"


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
