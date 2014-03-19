__author__ = 'jorge'

from sqlalchemy import Column, String, Integer
from app import db


class Director(db.Model):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)