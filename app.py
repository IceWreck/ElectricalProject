from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breach_time = db.Column(db.String, nullable=False)


@app.route('/', methods=["GET"])
def index():
    breach_history = History.query.all()
    return render_template('template.html', breach_history=breach_history)

@app.route('/hailhydra', methods=["GET"])
def nodemcu_endpoint():
    breach_time = datetime.now().strftime('%I:%M %p on %d-%B-%Y')
    breach = History(breach_time = breach_time)
    db.session.add(breach)
    db.session.commit()
    return "Hydra"
    