from sqlalchemy import Column, Integer, String, JSON, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .base import Base

class Problem(Base):
    __tablename__ = 'problem'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    writers = Column(ARRAY(JSON))
    editors = Column(ARRAY(JSON))
    source_name = Column(String)
    source_url = Column(String)

    submissions = relationship("Submission", back_populates="problem")