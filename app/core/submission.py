import app.repository as repo

def get_submission_by_id(session, id):
    return repo.get_submission_by_id(session, id)
