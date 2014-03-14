import os

CSRF_ENABLED = True
SECRET_KEY = 'PswAlvaroGarcia2013!'


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')