"""create problem_writing table

Revision ID: e791b9bc7450
Revises: 904fd119b6aa
Create Date: 2021-02-07 07:34:12.776369+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e791b9bc7450'
down_revision = '904fd119b6aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'problem_writing',
        sa.Column('account_id', sa.Integer, sa.ForeignKey('account.id')),
        sa.Column('problem_id', sa.Integer, sa.ForeignKey('problem.id')),)
        


def downgrade():
    op.drop_table('problem_writing')
