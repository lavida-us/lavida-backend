from graphene import Field, ObjectType, InputObjectType, ID, String

from app.schemas.type import Problem
from app.resolvers import resolve_update_problem

class UpdateProblemInput(InputObjectType):
    id = ID(required=True)
    title = String()
    source_name = String()
    source_url = String()

class MutateProblem(ObjectType):
    class Meta:
        abstract = True

    update_problem = Field(Problem, input=UpdateProblemInput())
    resolve_update_problem = resolve_update_problem
