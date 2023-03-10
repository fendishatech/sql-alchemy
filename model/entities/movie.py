# coding = utf-8

from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from helpers.base import Base

movies_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date) -> None:
        self.title = title
        self.release_date = release_date
