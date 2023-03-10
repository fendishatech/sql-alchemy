# coding = utf-8

from sqlalchemy import Column, String, Integer, Date

from helpers.base import Base


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday) -> None:
        self.name = name
        self.birthday = birthday
