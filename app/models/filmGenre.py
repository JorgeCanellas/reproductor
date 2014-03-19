__author__ = 'jorge'
from sqlalchemy import Column
from app import db


film_genre = db.Table('film_genre',
    Column('film_id', db.Integer, db.ForeignKey('Film.id')),
    Column('genre_id', db.Integer, db.ForeignKey('Genre.id'))
)
