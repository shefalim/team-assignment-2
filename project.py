import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'javaisanart'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teaminfo')
def members_page():
    return render_template('teaminfo.html')


if __name__ == '__main__':
    app.run(debug=True)
