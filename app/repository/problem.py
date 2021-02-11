from app.models import Problem

def get_problem_by_id(session, id):
    return session.query(Problem).get(id)

def update_problem_by_id(session, id, input):
    problem = session.query(Problem).get(id)
    if problem is None:
        return None
    problem.update(**input)
    session.commit()
    return problem
