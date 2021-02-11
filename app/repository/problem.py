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

def create_problem_by_id(session, input):
    problem = Problem.create(**input)
    session.add(problem)
    session.commit()
    return problem

def delete_problem_by_id(session, id):
    problem = session.query(Problem).get(id)
    if problem is None:
        return None
    session.delete(problem)
    session.commit()
    return problem
