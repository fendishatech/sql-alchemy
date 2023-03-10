# coding = utf-8

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

from helpers.base import Base


class Stunt(Base):
    __tablename__ = "stunts"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Boolean)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref=backref("stunt", uselist=False))

    def __init__(self, name, active, actor) -> None:
        self.name = name
        self.active = active
        self.actor = actor
