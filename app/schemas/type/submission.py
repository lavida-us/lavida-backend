import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models import Submission

class Submission(SQLAlchemyObjectType):
    class Meta:
        model = Submission
