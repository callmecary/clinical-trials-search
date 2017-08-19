"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from ClinicalTrails import app, api, Resource
import json, requests

@api.route('/<string:keywords>')
class HelloWorld(Resource):
    def get(self,keywords):
        url = 'https://clinicaltrialsapi.cancer.gov/v1/clinical-trials/'
        params = dict(
            _fulltext=keywords
        )
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        return data


