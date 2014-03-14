from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo, ValidationError, Email
from app import app, db, login_manager
from models import Monkey


class newFilmForm(Form):

	usernameSigin = TextField('Username', id = 'usernameSigin', validators = [Required(), validate_username])
	emailSigin = TextField('Email', id = 'emailSigin', validators = [Required(), Email(), validate_email])
	passwordSigin = PasswordField('Password', id = 'passwordSigin', validators = [Required(), EqualTo('password2Sigin', message='Password must match!')])
	password2Sigin = PasswordField('Repeat Password', id = 'password2Sigin',validators = [Required()])


	title = TextField('Title', id = 'titleFilm', validators = [Required()])
	genre = relationship("Genre", secondary=film_genre)
	runtime = Column(Integer)
	releaseDate = Column(DateTime())
	director = relationship("Director", secondary=direction)
	cast = relationship("Actor", secondary=casting)
	storyline = Column(String(800), unique = True)
	rating = Column(Integer)
	ageLimit = Column(Integer)
	cover = Column(String(120), unique = True)
	link = Column(String(120), unique = True)