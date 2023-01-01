from flask import Flask, request
from config import Config
from flask_bootstrap import Bootstrap
from flask_babel import Babel, lazy_gettext as _l
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler
import logging
import os

app = Flask(__name__)

# configuration for the application
app.config.from_object(Config)

# database instance
db = SQLAlchemy(app)

# manages the user logged-in state i.e keeps the user logged in
# when navigating different pages and even after closing the browser window
login = LoginManager(app)
# tells flask which page handles logins to enforce logging
login.login_view = 'login'
# override the default message when the user is redirected to the login page
login.login_message = _l('Please log in to access this page.')

# migration engine instance
migrate = Migrate(app, db)


# @app.before_first_request
# def create_tables():
#     db.create_all()


if not app.debug:
    # create a logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.mkdir('logs')
    # create an instance of Rotating FileHandler that ensures the log files don't grow too large
    # size of logs is limited to 10KB, and the last 10 log files are kept as backup
    file_handler = RotatingFileHandler(
        'logs/postit.log', maxBytes=10240, backupCount=10)
    # custom formatting for the log messages
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    # set the logging level of the file logger handler
    file_handler.setLevel(logging.INFO)

    # application logger
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('PostIt startup')

bootstrap = Bootstrap(app)
# instance of moment.js that converts UTC time to local timezone
moment = Moment(app)
# translates languages
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

# avoid circular imports
from app import errors, routes, models

