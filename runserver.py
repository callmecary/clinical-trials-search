"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from ClinicalTrails import app

if __name__ == '__main__':
    app.run(debug=True)