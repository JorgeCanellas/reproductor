from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref



film_genre = db.Table('film_genre',
    Column('film_id', db.Integer, db.ForeignKey('Film.id')),
    Column('genre_id', db.Integer, db.ForeignKey('Genre.id'))
)

casting = db.Table('casting',
    Column('film_id', db.Integer, db.ForeignKey('Film.id')),
    Column('actor_id', db.Integer, db.ForeignKey('Actor.id'))
)

direction = db.Table('direction',
    Column('film_id', db.Integer, db.ForeignKey('Film.id')),
    Column('director_id', db.Integer, db.ForeignKey('Director.id'))
)



class Film(db.Model):
	
	__tablename__ = "films"

	id = Column(Integer, primary_key=True)
	title = Column(String(120), unique = True)
	genre = relationship("Genre", secondary=film_genre)
	runtime = Column(Integer)
	releaseDate = Column(DateTime())
	director = relationship("Director", secondary=direction)
	cast = relationship("Actor", secondary=casting)
	storyline = Column(String(800), unique = True)
	rating = Column(Integer)
	languages = Column(String(120), unique = True)
	ageLimit = Column(Integer)
	cover = Column(String(120), unique = True)
	link = Column(String(120), unique = True)


class Genre(db.Model):

	__tablename__ = "genres"
	id = Column(Integer, primary_key=True)
	name = Column(String(120), unique = True)

class Actor(db.Model):

	__tablename__ = "actors"
	id = Column(Integer, primary_key=True)
	name = Column(String(120), unique = True)

class Director(db.Model):

	__tablename__ = "directors"
	id = Column(Integer, primary_key=True)
	name = Column(String(120), unique = True)