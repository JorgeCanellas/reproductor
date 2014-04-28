from app.models.direction import direction
from app.models.filmGenre import film_genre
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import Required, EqualTo, Email
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.models import casting


class GenreForm(Form):
    genre = SelectField(choices=['genre1', 'genre2'])


class FilmForm(Form):
    title = TextField('Title', id='titleFilm', validators=[Required()])
    genre = relationship("Genre", secondary=film_genre)
    runtime = Column(Integer)
    releaseDate = Column(DateTime())
    director = relationship("Director", secondary=direction)
    cast = relationship("Actor", secondary=casting)
    storyline = Column(String(800), unique=True)
    rating = Column(Integer)
    ageLimit = Column(Integer)
    cover = Column(String(120), unique=True)
    link = Column(String(120), unique=True)