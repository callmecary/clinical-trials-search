"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from ClinicalTrials import app, api, Resource
import json, requests
import db

ns = api.namespace('api', description='SEARCH operations')
parser = api.parser()
parser.add_argument('keywords', type=str, help='Keywords to search')
parser.add_argument('page_num', type=int, help='Page offset')
parser.add_argument('page_size', type=int, help='Limit per page')
@ns.route('/v1/search')
@ns.doc('search_by_keywords')
class search(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        data = db.search(args['keywords'],args['page_num'],args['page_size'])
        return data

@ns.route('/v1/contacts/<string:nct_id>')
@ns.doc('get_contacts_by_nctid')
class contacts(Resource):
    def get(self,nct_id):
        data = db.get_contacts_by_nctid(nct_id)
        return data