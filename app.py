from flask import Flask
from flask import request
import sys


sys.path.append("..")

app = Flask(__name__)
from handlers import person
