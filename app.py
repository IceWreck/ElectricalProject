from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breach_time = db.Column(db.String, nullable=False)


@app.route('/', methods=["GET"])
def index():
    breach_history = History.query.all()
    return render_template('index.html', breach_history=breach_history)

@app.route('/fuckyou', methods=["GET"])
def nodemcu_endpoint():
    breach_time = datetime.now().strftime('%H:%M on %d-%m-%Y')
    breach = History(breach_time = breach_time)
    db.session.add(breach)
    db.session.commit()
    return "FuckYou"


# Coment out this later
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5005)