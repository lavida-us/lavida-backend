import graphene

class Submission(graphene.ObjectType):
    id = graphene.ID()
    owned_user = graphene.Field('app.schemas.user.User')
    updated_at = graphene.DateTime()
    inserted_at = graphene.DateTime()
