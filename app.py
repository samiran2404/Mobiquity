from flask import Flask, request, jsonify, make_response
import datetime
import uuid

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/create_atm", methods=["POST"])
def create_atm():
    pass


@app.route("/get_atm/<city_name>", methods=["GET"])
def get_atm():
    pass


if __name__ == "__main__":
    app.run(debug=True)
