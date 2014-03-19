__author__ = 'jorge'
from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref


class Film(db.Model):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True)
    genre = relationship("Genre", secondary=film_genre)
    runtime = Column(Integer)
    releaseDate = Column(DateTime())
    director = relationship("Director", secondary=direction)
    cast = relationship("Actor", secondary=casting)
    storyline = Column(String(800), unique=True)
    rating = Column(Integer)
    languages = Column(String(120), unique=True)
    ageLimit = Column(Integer)
    cover = Column(String(120), unique=True)
    link = Column(String(120), unique=True)
