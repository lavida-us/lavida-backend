from flask_sqlalchemy import SQLAlchemy

from .account import Account
from .problem import Problem
from .submission import Submission

db = SQLAlchemy()

def init_app(app, config):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = config.db_host
    db.init_app(app)