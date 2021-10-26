import os
import time
from config import Cfg
from zappa import handler


def lambda_handler(event, context):
    print("Hello World")
    return handler.lambda_handler(event, context)
