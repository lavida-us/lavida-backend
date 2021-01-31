from datetime import datetime
import graphene

from .submission import Submission

class User(graphene.ObjectType):
    id = graphene.ID()
    user_id = graphene.String()
    name = graphene.String()
    profile_image = graphene.String()
    submissions = graphene.List(
        Submission,
        first=graphene.Int(),
        skip=graphene.Int(),
    )

    updated_at = graphene.DateTime()
    inserted_at = graphene.DateTime()

    def resolve_submissions(self, info, first=None, skip=None):
        return [Submission(1, self, datetime.now(), datetime.now())]