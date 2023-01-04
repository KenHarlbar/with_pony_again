#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.models import db, Amenity, City, Place, Review, State, User
from pony.orm import *

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                klass = classes[clss]
                with db_session:
                    objs = klass.select(lambda obj: obj)[:]
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def save(self):
        """commit all changes of the current database session"""
        commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            klass = obj.__class__.__name__
            with db_session:
                klass[obj.id].delete()

    def reload(self):
        """reloads data from the database"""
        db.bind(provider='mysql',
                  host='localhost',
                  user='hbnb_dev',
                  passwd='Hbnb_dev_pwd01#',
                  db='hbnb_dev_db')
        db.generate_mapping(create_tables=True)

    def close(self):
        """call remove() method on the private session attribute"""
        db.disconnect()
