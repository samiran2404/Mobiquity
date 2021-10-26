from flask import Flask, request, jsonify, make_response
import datetime
import uuid

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
