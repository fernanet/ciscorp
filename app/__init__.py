# app\__init__.py

# importações de terceiros
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# importações locais
from config import app_config

# inicialização da variável db
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # rota temporária
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
