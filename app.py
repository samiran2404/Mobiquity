from flask import Flask, request, jsonify, make_response
import datetime
from tools import Processor
import boto3
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
    processor = Processor()
    city_name = request.args.get("city_name")
    atm_list = processor.get_atm_list(city_name)
    return {
        "atm_list": atm_list
    }


if __name__ == "__main__":
    app.run(debug=True)
