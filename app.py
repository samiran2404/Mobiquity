from flask import Flask, request, jsonify, make_response
import datetime
from tools import Processor
import boto3
import uuid
import json
from config import constants, Cfg
import os

app = Flask(__name__)

CONF = Cfg(os.environ.get(constants.STAGE))


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/create_atm", methods=["POST"])
def create_atm():
    return jsonify(request.json)


@app.route("/get_atm", methods=["GET"])
def get_atm():
    processor = Processor()
    city_name = request.args.get("city_name")
    print(city_name)
    atm_list = processor.get_atm_list(city_name)
    return jsonify({"atm": atm_list})


if __name__ == "__main__":
    app.run(debug=True)
