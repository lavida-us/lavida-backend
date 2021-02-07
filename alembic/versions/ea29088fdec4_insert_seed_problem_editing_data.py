"""insert seed problem_editing data

Revision ID: ea29088fdec4
Revises: 16bbc9c1485e
Create Date: 2021-02-07 07:40:17.511456+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea29088fdec4'
down_revision = '16bbc9c1485e'
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('problem_editing',))
    problem_editing_table_tbl = sa.Table('problem_editing', meta)

    op.bulk_insert(
        problem_editing_table_tbl,
        [
            {
                'account_id': 2,
                'problem_id': 2
            }
        ]
    )


def downgrade():
    pass
