from flask import Flask
from flask_scss import Scss
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
Scss(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

