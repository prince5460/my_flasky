# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-2-27 下午4:45
@Desc :
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
