from flask import Flask, render_template, request, Response, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_weasyprint import HTML, render_pdf

import ast
import json
import dicttoxml
from datetime import datetime

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


@app.route('/api/report/<int:id>.xml/')
def get_xml_report(id):
    report = Reports.query.get(id)
    obj = json.loads(report.type)
    xml = dicttoxml.dicttoxml(obj)
    return Response(xml, mimetype='text/xml')


@app.route('/api/report/<int:id>.pdf')
def get_pdf_report(id):
    # Make a PDF from another view
    report = ast.literal_eval(Reports.query.get(id).type)
    report['created']  = datetime.now().strftime('%Y-%m-%d') # timestamp
    html = render_template('report.html',report= report)
    return render_pdf(HTML(string=html))

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == "__main__":
    app.run()