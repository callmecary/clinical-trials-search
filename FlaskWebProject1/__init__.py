"""
The flask application package.
"""

from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

import FlaskWebProject1.views
