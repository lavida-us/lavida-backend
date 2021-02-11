from app import core

def resolve_account(parent, info, input):
    session = info.context['session']
    id = input.id

    return core.get_account_by_id(session, id)

def resolve_update_account(parent, info, input):
    session = info.context['session']
    id = input.id

    return core.update_account_by_id(session, id, vars(input))
