#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""engine DBStorage connecting to MysqlAlchemy"""

__engine = None
__session = None


class DBStorage:
    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}".format(user, pwd, host, db),
            pool_pre_ping=True,)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """A method that gets all the objects of cls if not
        None, otherwise it gets all the objects of all classes"""
        all_objects = {}
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]
        for cls in classes:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                all_objects[key] = obj
        return all_objects

    def new(self, obj):
        """ add the object to the current database session """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """  delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """A method that reloads a session. saves all the tables
        and it uses scoped session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """ calls remove()
        """
        self.__session.remove()
