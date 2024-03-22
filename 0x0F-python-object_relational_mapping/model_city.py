#!/usr/bin/python3

""" Python file containing class definition of a State and instance Base """

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class City(Base):
    """ Class with attributes of a city """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
