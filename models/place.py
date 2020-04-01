#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.review import Review
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    """ metadata = Base.metadata

    place_amenity = Table(
        'place_amenity', metadata,
        Column('place_id', String(60),
               ForeignKey('places.id'),
               primary_key=True,
               nullable=False),
        Column('amenity_id', String(60),
               ForeignKey('amenities.id'),
               primary_key=True,
               nullable=False)) """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place')

    @property
    def reviews(self):
        """returns a list of  review instances with place_id"""
        review_list = []

        for key, value in models.storage().all():
            inst = key.split('.')
            name_inst = inst[0]
            if name_inst == "Review":
                if value.place_id == self.id:
                    review_list.append(value)
        return review_list

    @property
    def amenities(self):
        """
        Returns the list of Amenity instances
        based on the attribute amenity_ids
        """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """
        Add id to amenity_ids
        """
        if isinstance(obj, 'Amenities'):
            self.amenity_ids.append(obj.id)
