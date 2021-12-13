from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Configuration for the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqllite:///prize.db'

db = SQLAlchemy(app)

from application import routes