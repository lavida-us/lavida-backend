from sqlalchemy import Column, Integer, String, JSON, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy.types as types

from .base import Base
from .association import association_table_problem_writing, association_table_problem_editing

class Problem(Base):
    __tablename__ = 'problem'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    source_name = Column(String)
    source_url = Column(String)

    writers = relationship("Account", secondary=association_table_problem_writing)
    editors = relationship("Account", secondary=association_table_problem_editing)
    submissions = relationship("Submission", back_populates="problem")