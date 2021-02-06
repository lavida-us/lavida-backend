from graphene import Field, ObjectType, InputObjectType, ID

from app.schemas.type.account import Account
from app.resolvers.account import resolve_account

class AccountInput(InputObjectType):
    id = ID(required=True)

class QueryAccount(ObjectType):
    class Meta:
        abstract = True

    account = Field(Account, input=AccountInput())
    resolve_account = resolve_account
