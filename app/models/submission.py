import enum

from sqlalchemy import Column, Integer, String, JSON, ARRAY, Float, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .base import Base

class Status(enum.Enum):
    pending = 1
    judging = 2
    judged = 3

class Result(enum.Enum):
    accept = 1
    wrong_answer = 2
    time_limit_exceed = 3
    memory_limit_exceed = 4
    compile_error = 5
    runtime_error = 6

class Submission(Base):
    __tablename__ = 'submission'
    id = Column(Integer, primary_key=True)
    owned_account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    owned_account = relationship("Account", back_populates="submissions")
    problem_id = Column(Integer, ForeignKey('problem.id'), nullable=False)
    problem = relationship("Problem", back_populates="submissions")
    status = Column(Enum(Status), nullable=False)
    result = Column(Enum(Result))
    time = Column(Float)
    memory = Column(Float)
    programming_language = Column(String)

    inserted_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
