"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app, api, Resource
import requests
import json

@api.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        r=requests.post('https://clinicaltrialsapi.cancer.gov/v1/clinical-trials',data={"sites.org_state_or_province": ["NY"],"record_verification_date_gte": "2017-06-01","include": ["nci_id"]})
        json_data = json.loads(r.text)
        return json_data

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
