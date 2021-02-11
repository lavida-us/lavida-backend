import app.repository as repo

def get_account_by_id(session, id):
    return repo.get_account_by_id(session, id)
