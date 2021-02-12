"""add field timestamp on problem_editing

Revision ID: 662fd971e819
Revises: dca4ff85daa4
Create Date: 2021-02-12 07:11:59.929624+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '662fd971e819'
down_revision = 'dca4ff85daa4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('problem_editing',
        sa.Column('inserted_at', sa.TIMESTAMP, server_default=sa.func.now())
    )


def downgrade():
    op.drop_column('problem_editing', 'inserted_at')
