"""add field timestamp on Problem

Revision ID: 950da200356d
Revises: 4000e84d2595
Create Date: 2021-02-12 07:07:41.331049+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950da200356d'
down_revision = '4000e84d2595'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('problem',
        sa.Column('inserted_at', sa.TIMESTAMP, server_default=sa.func.now())
    )
    op.add_column('problem',
        sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_column('problem', 'inserted_at')
    op.drop_column('problem', 'updated_at')
