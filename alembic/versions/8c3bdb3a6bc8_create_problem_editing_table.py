"""create problem_editing table

Revision ID: 8c3bdb3a6bc8
Revises: e791b9bc7450
Create Date: 2021-02-07 07:36:31.852481+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c3bdb3a6bc8'
down_revision = 'e791b9bc7450'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'problem_editing',
        sa.Column('account_id', sa.Integer, sa.ForeignKey('account.id')),
        sa.Column('problem_id', sa.Integer, sa.ForeignKey('problem.id')),)


def downgrade():
    op.drop_table('problem_editing')
