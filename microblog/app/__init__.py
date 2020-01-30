from flask import Flask
from flask_scss import flask_scss

app = Flask(__name__)
Scss(app)

from app import routes
