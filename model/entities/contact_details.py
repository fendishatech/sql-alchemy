# coding = utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from helpers.base import Base


class ContactDetail(Base):
    __tablename__ = "contact_details"

    id = Column(Integer, primary_key=True)
    phone_no = Column(String)
    address = Column(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref="contact_details")

    def __init__(self, phone_no, address, actor) -> None:
        self.phone_no = phone_no
        self.address = address
        self.actor = actor
