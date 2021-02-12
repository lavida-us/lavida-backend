from graphene import Field, ObjectType, InputObjectType, ID

from app.schemas.type import Submission
from app.resolvers import resolve_get_submission

class GetSubmissionInput(InputObjectType):
    id = ID(required=True)

class QuerySubmission(ObjectType):
    class Meta:
        abstract = True

    get_submission = Field(Submission, input=GetSubmissionInput())
    resolve_get_submission = resolve_get_submission
