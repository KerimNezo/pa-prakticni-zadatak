from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"

from ProductArena import routes
import requests