from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .base import Base

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    login = Column(String(128), nullable=False)
    email = Column(String(128))
    univ = Column(String(128))
    profile_nickname = Column(String(128))
    profile_image = Column(String(65536))

    submissions = relationship("Submission", back_populates="owned_account")