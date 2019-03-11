import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    picture = Column(String(300))


class ShoeCompanyName(Base):
    __tablename__ = 'shoecompanyname'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="shoecompanyname")

    @property
    def serialize(self):
        """Return objects data in easily serializeable formats"""
        return {
            'name': self.name,
            'id': self.id
        }


class ShoeNames(Base):
    __tablename__ = 'shoenames'
    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)
    sole = Column(String(150))
    closure = Column(String(150))
    material = Column(String(150))
    lifestyle = Column(String(10))
    price = Column(String(250))
    date = Column(DateTime, nullable=False)
    shoecompanynameid = Column(Integer, ForeignKey('shoecompanyname.id'))
    shoecompanyname = relationship(
        ShoeCompanyName, backref=backref('shoenames', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="shoenames")

    @property
    def serialize(self):
        """Return objects data in easily serializeable formats"""
        return {
            'name': self. name,
            'sole': self. sole,
            'closure': self. closure,
            'material': self. material,
            'lifestyle': self. lifestyle,
            'price': self. price,
            'date': self. date,
            'id': self. id
        }

engin = create_engine('sqlite:///shoes.db')
Base.metadata.create_all(engin)
