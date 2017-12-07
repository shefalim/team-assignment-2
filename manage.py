from flask_script import Manager
from project import app, db, Director, Movie

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    director1 = Director(first_name='Jon', last_name='Favreau')
    director2 = Director(first_name='Chris', last_name='Columbus')
    director3 = Director(first_name='Richard', last_name='Curtis')
    movie1 = Movie(title='Elf', director=director1, year='2003', genre='Comedy')
    movie2 = Movie(title='Home Alone', director=director2, year='1990', genre='Comedy')
    movie3 = Movie(title='Love Actually', director=director3, year='2003', genre='Romance')
    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
