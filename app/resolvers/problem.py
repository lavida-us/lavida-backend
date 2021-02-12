from app import core

def resolve_get_problem(parent, info, input):
    session = info.context['session']
    id = input.id

    return core.get_problem_by_id(session, id)

def resolve_update_problem(parent, info, input):
    session = info.context['session']
    id = input.id

    return core.update_problem_by_id(session, id, vars(input))

def resolve_create_problem(parent, info, input):
    session = info.context['session']
    if input.writer_ids is None:
        input.writer_ids = []
    if input.editor_ids is None:
        input.editor_ids = []
    return core.create_problem_by_id(session, vars(input))

def resolve_delete_problem(parent, info, input):
    session = info.context['session']
    id = input.id

    return core.delete_problem_by_id(session, id)
