#!/usr/bin/python

from pony.orm import *
from datetime import datetime
from uuid import UUID, uuid4


db = Database()


class Review(db.Entity):
    _table_ = 'reviews'
    id = PrimaryKey(str, default=lambda: str(uuid4()))
    created_at = Required(datetime, default=datetime.now())
    updated_at = Required(datetime, default=datetime.now(), index=True)
    text = Required(str)
    user_id = Required('User')
    place_id = Required('Place')


class User(db.Entity):
    _table_ = 'users'
    id = PrimaryKey(str, default=lambda: str(uuid4()))
    created_at = Required(datetime, default=datetime.now())
    updated_at = Required(datetime, default=datetime.now(), index=True)
    email = Required(str, unique=True)
    password = Required(str)
    first_name = Optional(str)
    last_name = Optional(str)
    reviews = Set(Review)
    places = Set('Place')


class Place(db.Entity):
    _table_ = 'places'
    id = PrimaryKey(str, default=lambda: str(uuid4()))
    created_at = Required(datetime, default=datetime.now())
    updated_at = Required(datetime, default=datetime.now(), index=True)
    name = Required(str)
    description = Optional(str)
    number_rooms = Required(int, default=0)
    number_bathrooms = Required(int, default=0)
    max_guest = Required(int, default=0)
    price_by_night = Required(int, default=0)
    latitude = Optional(float)
    longitude = Optional(float)
    reviews = Set(Review)
    user_id = Required(User)
    city_id = Required('City')
    place_amenitys = Set('PlaceAmenity')


class Amenity(db.Entity):
    _table_ = 'amenities'
    id = PrimaryKey(str, default=lambda: str(uuid4()))
    created_at = Required(datetime, default=datetime.now())
    updated_at = Required(datetime, default=datetime.now(), index=True)
    name = Required(str)
    place_amenitys = Set('PlaceAmenity')


class State(db.Entity):
    _table_ = 'states'
    id = PrimaryKey(str, default=lambda: str(uuid4()))
    created_at = Required(datetime, default=datetime.now())
    updated_at = Required(datetime, default=datetime.now(), index=True)
    name = Required(str)
    citys = Set('City')


class City(db.Entity):
    _table_ = 'cities'
    id = PrimaryKey(str, default=lambda: str(uuid4()))
    created_at = Required(datetime, default=datetime.now())
    updated_at = Required(datetime, default=datetime.now(), index=True)
    name = Required(str)
    state_id = Required(State)
    places = Set(Place)


class PlaceAmenity(db.Entity):
    _table_ = 'place_amenities'
    amenities = Required(Amenity)
    places = Required(Place)
    PrimaryKey(amenities, places)
