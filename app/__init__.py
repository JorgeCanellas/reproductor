import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir


app = Flask(__name__)
app.config.from_object('config')


# SQLAlchemy

db = SQLAlchemy(app)

# Login Manager

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


from app import view, models
from app.models import *
from app.views import importFilm
