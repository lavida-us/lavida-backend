from app import core

def resolve_submission(parent, info, input):
    session = info.context['session']
    id = input.id

    return core.get_submission_by_id(session, id)
