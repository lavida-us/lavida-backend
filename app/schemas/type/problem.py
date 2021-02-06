import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models import Problem

class Problem(SQLAlchemyObjectType):
    class Meta:
        model = Problem
