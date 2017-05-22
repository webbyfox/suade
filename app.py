from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask import jsonify

from model import Reports

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://interview:LetMeIn@candidate.suade.org/suade'
db = SQLAlchemy(app)
db.init_app(app)

@app.route("/")
def hello():
    return "Welcome to Suade Reporting API!"




@app.route('/api/reports/', methods=['GET'])
def get_all_reports():
    reports = Reports.query.all()
    return jsonify([item.type for item in reports])

@app.route('/api/report/<int:id>/', methods=['GET'])
def get_report(id):
    report = Reports.query.get(id)
    return report.type

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.run()