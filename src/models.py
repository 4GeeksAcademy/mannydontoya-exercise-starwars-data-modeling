import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    height = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=True)
    population = Column(String(250), nullable=True)
    gravity = Column(String(250), nullable=True)
    rotation_period = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=True)




class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
