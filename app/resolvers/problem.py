from app.models import Problem

def resolve_problem(parent, info, input):
    session = info.context['session']
    id = input.id

    return session.query(Problem).get(id)