from flask import Flask
from flask_scss import Scss

app = Flask(__name__)
Scss(app)

from app import routes
