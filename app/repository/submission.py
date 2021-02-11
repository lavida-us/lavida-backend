from app.models import Submission

def get_submission_by_id(session, id):
    return session.query(Submission).get(id)
