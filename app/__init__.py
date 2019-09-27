from flask import Flask
from .config import DevConfig

#Initializing application
app = Flask(__name__)

#Setup app configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config')

from app import views

