"""insert seed submission data

Revision ID: 904fd119b6aa
Revises: f37115dce4c2
Create Date: 2021-02-06 05:57:10.200974+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '904fd119b6aa'
down_revision = 'f37115dce4c2'
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('submission',))
    submission_table_tbl = sa.Table('submission', meta)

    op.bulk_insert(
        submission_table_tbl,
        [
            {
                'owned_account_id': 1,
                'problem_id': 1,
                'status': 'judged',
                'result': 'accept',
                'time': 0.834,
                'memory': 100.12,
                'programming_language': 'C++'
            },
            {
                'owned_account_id': 2,
                'problem_id': 1,
                'status': 'judged',
                'result': 'accept',
                'time': 1.543,
                'memory': 250.2,
                'programming_language': 'Python'
            },
            {
                'owned_account_id': 1,
                'problem_id': 2,
                'status': 'judged',
                'result': 'wrong_answer',
                'time': 0.143,
                'memory': 120.8,
                'programming_language': 'C++'
            },
        ]
    )


def downgrade():
    pass
