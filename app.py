import os
from dotenv import load_dotenv
from flask import Flask
from flask_mailman import Mail
from models import db
from routes import site
from auth import auth
from admin import admin
from create_db import create_db
load_dotenv()

project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'static')
un = os.getenv("DB_USERNAME")
pw = os.getenv("DB_PASSWORD")
hn = os.getenv("DB_HOSTNAME")
dt = os.getenv("DB_DATABASE")


def create_app():
    app = Flask(__name__, instance_path=project_root, template_folder=template_path, static_folder=static_path)
    app.config.update(
        SITE_NAME=os.getenv("SITE_NAME"),
        SQLALCHEMY_DATABASE_URI="mysql://" + un + ":" + pw + "@" + hn + "/" + dt,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        RECAPTCHA_PUBLIC_KEY=os.getenv("RECAPTCHA_PUBLIC_KEY"),
        RECAPTCHA_PRIVATE_KEY=os.getenv("RECAPTCHA_PRIVATE_KEY"),
        SECRET_KEY=os.getenv("SECRET_KEY"),
        MAIL_SERVER=os.getenv("MAIL_SERVER"),
        MAIL_PORT=os.getenv("MAIL_PORT"),
        MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
        MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
        MAIL_USE_TLS=False,
        MAIL_USE_SSL=True,
    )
    app.register_blueprint(site)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    db.init_app(app)
    Mail(app)
    with app.app_context():
        create_db()
        db.create_all()
    return app


application = create_app()
