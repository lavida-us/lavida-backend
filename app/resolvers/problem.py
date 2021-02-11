from app import core

def resolve_problem(parent, info, input):
    session = info.context['session']
    id = input.id

    return core.get_problem_by_id(session, id)

def resolve_update_problem(parent, info, input):
    session = info.context['session']
    id = input.id

    return core.update_problem_by_id(session, id, vars(input))
