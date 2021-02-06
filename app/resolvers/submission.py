from app.models import Submission

def resolve_submission(parent, info, input):
    session = info.context['session']
    id = input.id

    return session.query(Submission).get(id)