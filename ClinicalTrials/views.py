"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from ClinicalTrials import app, api, Resource
import json, requests
#import db

@api.route('/<string:keywords>&<int:page_num>&<int:page_size>')
class Search(Resource):
    def get(self,keywords,page_num,page_size):
        #data = db.search(keywords,page_num,page_size)
        #return data
        return 'comming soon.'

