import graphene
from app.schemas.graphql_view import LavidaGraphQLView
from datetime import datetime

from .query import QueryAccount, QueryProblem, QuerySubmission

class Query(QueryAccount, QueryProblem, QuerySubmission):
    pass

schema = graphene.Schema(query=Query)

def init_app(app, config):
    app.add_url_rule(
        "/graphql",
        view_func=LavidaGraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )