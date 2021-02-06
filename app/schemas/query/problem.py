from graphene import Field, ObjectType, InputObjectType, ID

from app.schemas.type import Problem
from app.resolvers import resolve_problem

class ProblemInput(InputObjectType):
    id = ID(required=True)

class QueryProblem(ObjectType):
    class Meta:
        abstract = True

    problem = Field(Problem, input=ProblemInput())
    resolve_problem = resolve_problem
