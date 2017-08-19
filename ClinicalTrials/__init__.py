"""
The flask application package.
"""

from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app, version='1.0', title='Mars API',
    description='A global clinical trials API',
)

import ClinicalTrials.views
