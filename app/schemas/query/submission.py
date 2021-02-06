from graphene import Field, ObjectType, InputObjectType, ID

from app.schemas.type import Submission
from app.resolvers import resolve_submission

class SubmissionInput(InputObjectType):
    id = ID(required=True)

class QuerySubmission(ObjectType):
    class Meta:
        abstract = True

    submission = Field(Submission, input=SubmissionInput())
    resolve_submission = resolve_submission
