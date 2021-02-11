from app.models import Problem

def get_problem_by_id(session, id):
    return session.query(Problem).get(id)
