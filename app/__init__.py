from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

def create_app(config_name):

    #Initializing application
    app = Flask(__name__)

    #Setup app configuration
    app.config.from_object(DevConfig)
    #Initializing Bootstrap
    bootstrap = Bootstrap(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


