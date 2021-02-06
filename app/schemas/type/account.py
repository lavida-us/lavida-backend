import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models import Account

class Account(SQLAlchemyObjectType):
    class Meta:
        model = Account
