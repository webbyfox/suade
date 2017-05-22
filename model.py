from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://interview:LetMeIn@candidate.suade.org/suade'
db = SQLAlchemy(app)
db.init_app(app)


class Reports (db.Model):
 	id = db.Column(db.Integer, primary_key = True)
 	type =  db.Column(db.String(970))