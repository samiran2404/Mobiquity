from configparser import ConfigParser
import boto3
import logging
from config import constants
import sqlite3

PROJECT_NAME = 'mobiquity'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cfg(object, metaclass=Singleton):
    def get_parameter(self, name, decrypt=False):
        if self.stage == constants.LOCAL:
            return name
        return boto3.client('ssm', region_name='ap-southeast-1').get_parameters(Names=[name], WithDecryption=decrypt)["Parameters"][0]["Value"]

    def __init__(self, stage):
        self.stage = stage
        configp = ConfigParser()
        configp.read("config/" + stage + ".ini")
        self.Config = configp.get

        format = '%(lineno)d,  %(message)s'
        logging.basicConfig(format=format)
        self.logger = logging.getLogger("mobiquity")

        self.source = self.Config('source', 'source')
        self.dynamodb = boto3.client("dynamodb")
        self.table_name = self.Config('dynamodb', 'table_name')
