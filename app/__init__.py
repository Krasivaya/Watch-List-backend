from flask import Flask
from .config import DevConfig

#Initializing application
app = Flask(__name__, instace_relative_config = True)

#Setup app configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

