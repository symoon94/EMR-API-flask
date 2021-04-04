from flask import Flask
import sys
from flask import request

sys.path.append("..")

app = Flask(__name__)

from handlers import person

