from graphene import Field, ObjectType, InputObjectType, ID

from app.schemas.type.account import Account
from app.resolvers.account import resolve_get_account

class GetAccountInput(InputObjectType):
    id = ID(required=True)

class QueryAccount(ObjectType):
    class Meta:
        abstract = True

    get_account = Field(Account, input=GetAccountInput())
    resolve_get_account = resolve_get_account
