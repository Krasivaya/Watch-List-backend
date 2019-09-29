from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#Initializing application
app = Flask(__name__, instance_relative_config = True)

#Setup app configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing Bootstrap
bootstrap = Bootstrap(app)

from app import views

