import app.repository as repo

def get_problem_by_id(session, id):
    return repo.get_problem_by_id(session, id)

def update_problem_by_id(session, id, input):
    return repo.update_problem_by_id(session, id, input)

def create_problem_by_id(session, input):
    input['writers'] = map(lambda id: repo.get_account_by_id(session, id), input['writer_ids'])
    input['editors'] = map(lambda id: repo.get_account_by_id(session, id), input['editor_ids'])
    return repo.create_problem_by_id(session, input)
