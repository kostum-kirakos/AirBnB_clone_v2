#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from models.city import City
from os import getenv
from sqlalchemy.orm import relationship
from models import storage

STORAGE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Returns the cities"""
            cities_list = []
            for key, value in storage.all(City).items():
                if self.id == value.state_id:
                    cities_list.append(value)
            return cities_list
