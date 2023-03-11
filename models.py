from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    role = db.Column(db.String(255), nullable=False)


class Page(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(255))
    author = db.Column(db.String(255))
    title = db.Column(db.String(255))
    text = db.Column(db.String(64000))
    image_path = db.Column(db.String(255))
    emgithub = db.Column(db.String(255))
    youtube = db.Column(db.String(255))
    type = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    keywords = db.Column(db.String(255))
