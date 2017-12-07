import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'javaisanart'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.Text)
    movies = db.relationship('Movie', backref='director', cascade="delete")


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer)
#    director_id = db.Column(db.String(256))
    year = db.Column(db.Integer)
    genre = db.Column(db.Text)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teaminfo')
def members_page():
    return render_template('teaminfo.html')

@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)

@app.route('/movie/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('movie-add.html')
    if request.method == 'POST':
        title = request.form['title']
        director_id = request.form['director_id']
        year = request.form['year']
        genre = request.form['genre']
        movie = Movie(title=title, director_id=director_id, year=year, genre=genre)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/directors')
def show_all_directors():
    directors = Director.query.all()
    return render_template('director-all.html', directors=directors)

@app.route('/director/add', methods=['GET', 'POST'])
def add_director():
    if request.method == 'GET':
        return render_template('director-add.html')
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        director = Director(first_name=first_name, last_name=last_name)
        db.session.add(director)
        db.session.commit()
        return redirect(url_for('show_all_directors'))

if __name__ == '__main__':
    app.run(debug=True)
