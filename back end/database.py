from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Create database object
db = SQLAlchemy()

def init_db(app: Flask):
    """Initialize database with Flask app."""
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Create tables if not exist
    with app.app_context():
        db.create_all()
