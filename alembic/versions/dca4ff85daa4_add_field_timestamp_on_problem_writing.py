"""add field timestamp on problem_writing

Revision ID: dca4ff85daa4
Revises: 31bdb4dcddc5
Create Date: 2021-02-12 07:10:54.457316+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dca4ff85daa4'
down_revision = '31bdb4dcddc5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('problem_writing',
        sa.Column('inserted_at', sa.TIMESTAMP, server_default=sa.func.now())
    )


def downgrade():
    op.drop_column('problem_writing', 'inserted_at')
