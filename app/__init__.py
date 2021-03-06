# app/__init__.py

# importações de terceiros
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# importações locais
from config import app_config

# inicialização da variável db
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # rota temporária
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    login_manager.init_app(app)
    login_manager.login_message = "Você precisa estar logado para acessar esta página."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
