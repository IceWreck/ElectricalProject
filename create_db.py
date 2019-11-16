from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breach_time = db.Column(db.String, nullable=False)

def main():
    # Create tables based on each table definition in `models`
    db.create_all()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()