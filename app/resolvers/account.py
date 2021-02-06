from app.models import Account

def resolve_account(parent, info, input):
    session = info.context['session']
    id = input.id

    return session.query(Account).get(id)