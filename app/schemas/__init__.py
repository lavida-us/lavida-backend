import graphene
from flask_graphql import GraphQLView
from datetime import datetime

from .user import User

class Query(graphene.ObjectType):
    get_user = graphene.Field(User)

    def resolve_get_user(self, info):
        return {
            'id': 1,
            'user_id': 'pengsoo.ebs',
            'name': 'pengsoo',
            'profile_image': 'http://profile-image.com',
            'inserted_at': datetime.now(),
            'updated_at': datetime.now()
            }

schema = graphene.Schema(query=Query)

def init_app(app, config):
    app.add_url_rule("/graphql", view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))