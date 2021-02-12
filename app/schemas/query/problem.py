from graphene import Field, ObjectType, InputObjectType, ID

from app.schemas.type import Problem
from app.resolvers import resolve_get_problem

class GetProblemInput(InputObjectType):
    id = ID(required=True)

class QueryProblem(ObjectType):
    class Meta:
        abstract = True

    get_problem = Field(Problem, input=GetProblemInput())
    resolve_get_problem = resolve_get_problem
