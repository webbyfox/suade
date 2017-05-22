from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'ppostgres://interview:LetMeIn@candidate.suade.org/suade'
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Welcome to Suade Reporting API!"


if __name__ == "__main__":
    app.run()