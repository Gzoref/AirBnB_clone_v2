#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from models.base_model import BaseModel, Base
#from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        __tablename__: name for db table
        cities: relation with city
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete',
                              backref='state')
    else:
        @property
        def cities(self):
            """Returns the list of City instances with
            state_id equals to the current State.id
            city_list: list of cities from a state
            """
            from models import storage
            from models.city import City

            city_list = []
            city_dict = storage.all(City)

            #for key, value in storage.all(State):
            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
