from app.models import Account

def get_account_by_id(session, id):
    return session.query(Account).get(id)

def update_account_by_id(session, id, input):
    account = session.query(Account).get(id)
    account.update(**input)
    session.commit()
    return account
