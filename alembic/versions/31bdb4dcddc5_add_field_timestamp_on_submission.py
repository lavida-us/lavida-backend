"""add field timestamp on submission

Revision ID: 31bdb4dcddc5
Revises: 950da200356d
Create Date: 2021-02-12 07:09:53.514121+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31bdb4dcddc5'
down_revision = '950da200356d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('submission',
        sa.Column('inserted_at', sa.TIMESTAMP, server_default=sa.func.now())
    )
    op.add_column('submission',
        sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_column('submission', 'inserted_at')
    op.drop_column('submission', 'updated_at')
