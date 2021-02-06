from flask_graphql import GraphQLView
from graphene import ResolveInfo
from app.models import db

class LavidaGraphQLView(GraphQLView):
    def get_context(self):
        # context = super().get_context()

        return {'session': db.session}