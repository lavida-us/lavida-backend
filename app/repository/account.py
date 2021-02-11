from app.models import Account

def get_account_by_id(session, id):
    return session.query(Account).get(id)
