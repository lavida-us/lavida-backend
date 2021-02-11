import app.repository as repo

def get_problem_by_id(session, id):
    return repo.get_problem_by_id(session, id)
