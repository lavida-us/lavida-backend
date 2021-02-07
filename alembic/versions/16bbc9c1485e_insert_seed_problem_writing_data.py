"""insert seed problem_writing data

Revision ID: 16bbc9c1485e
Revises: 8c3bdb3a6bc8
Create Date: 2021-02-07 07:40:09.806391+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16bbc9c1485e'
down_revision = '8c3bdb3a6bc8'
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('problem_writing',))
    problem_writing_table_tbl = sa.Table('problem_writing', meta)

    op.bulk_insert(
        problem_writing_table_tbl,
        [
            {
                'account_id': 1,
                'problem_id': 1
            }
        ]
    )


def downgrade():
    pass
