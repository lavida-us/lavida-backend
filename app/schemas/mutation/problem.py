from graphene import Field, ObjectType, InputObjectType, ID, String, List, NonNull

from app.schemas.type import Problem
from app.resolvers import resolve_update_problem, resolve_create_problem

class UpdateProblemInput(InputObjectType):
    id = ID(required=True)
    title = String()
    source_name = String()
    source_url = String()

class CreateProblemInput(InputObjectType):
    title = String(required=True)
    source_name = String()
    source_url = String()
    writer_ids = List(NonNull(ID))
    editor_ids = List(NonNull(ID))

class MutateProblem(ObjectType):
    class Meta:
        abstract = True

    update_problem = Field(Problem, input=UpdateProblemInput())
    resolve_update_problem = resolve_update_problem

    create_problem = Field(Problem, input=CreateProblemInput())
    resolve_create_problem = resolve_create_problem
