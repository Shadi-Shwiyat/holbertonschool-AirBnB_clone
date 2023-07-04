#!/usr/bin/python3
""" Module class Amenity """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
