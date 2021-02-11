from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .base import Base
from .association import association_table_problem_writing, association_table_problem_editing

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    login = Column(String(128), nullable=False)
    email = Column(String(128))
    univ = Column(String(128))
    profile_nickname = Column(String(128))
    profile_image = Column(String(65536))

    written_problems = relationship("Problem", secondary=association_table_problem_writing)
    edited_problems = relationship("Problem", secondary=association_table_problem_editing)
    submissions = relationship("Submission", back_populates="owned_account")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None and key in Account.update.update_attr:
                setattr(self, key, value)
    update.update_attr = ['email', 'univ', 'profile_nickname', 'profile_image']