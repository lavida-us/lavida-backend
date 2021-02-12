from sqlalchemy import Table, Column, ForeignKey, Integer, TIMESTAMP
from .base import Base

association_table_problem_writing = Table('problem_writing', Base.metadata,
    Column('account_id', Integer, ForeignKey('account.id')),
    Column('problem_id', Integer, ForeignKey('problem.id')),
    Column('inserted_at', TIMESTAMP)
)

association_table_problem_editing = Table('problem_editing', Base.metadata,
    Column('account_id', Integer, ForeignKey('account.id')),
    Column('problem_id', Integer, ForeignKey('problem.id')),
    Column('inserted_at', TIMESTAMP)
)