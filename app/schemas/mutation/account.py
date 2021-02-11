from graphene import Field, ObjectType, InputObjectType, ID, String

from app.schemas.type import Account
from app.resolvers import resolve_update_account

class UpdateAccountInput(InputObjectType):
    id = ID(required=True)
    email = String()
    univ = String()
    profile_nickname = String()
    profile_image = String()

class MutateAccount(ObjectType):
    class Meta:
        abstract = True

    update_account = Field(Account, input=UpdateAccountInput())
    resolve_update_account = resolve_update_account
