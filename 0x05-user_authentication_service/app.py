#!/usr/bin/env python3
""" Appy flask navigator module """
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_message() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
