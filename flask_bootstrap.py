from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@server/db'
db = SQLAlchemy(app)


class contact(db.Model):
    S_no = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), unique=True, nullable=False)
    Email = db.Column(db.String(50), unique=True, nullable=False)
    Email = db.Column(db.String(50), unique=True, nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():

    return render_template('about.html')


@app.route("/contact")
def contact():

    return render_template('contact.html')


app.run(host='0.0.0.0', port=8080, debug=True)
