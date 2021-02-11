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

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None and key in Problem.update.update_attr:
                setattr(self, key, value)
    update.update_attr = ['title', 'source_name', 'source_url']

    def create(**kwargs):
        problem = Problem()
        problem.update(**kwargs)
        problem.writers.extend(kwargs['writers'])
        problem.editors.extend(kwargs['editors'])
        return problem
