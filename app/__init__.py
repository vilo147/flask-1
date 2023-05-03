from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import models, views

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object("config.Config")


db.create_all()