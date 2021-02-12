"""add field timestamp on Account

Revision ID: 4000e84d2595
Revises: ea29088fdec4
Create Date: 2021-02-12 06:27:59.930634+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4000e84d2595'
down_revision = 'ea29088fdec4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account',
        sa.Column('inserted_at', sa.TIMESTAMP, server_default=sa.func.now())
    )
    op.add_column('account',
        sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade():
    op.drop_column('account', 'inserted_at')
    op.drop_column('account', 'updated_at')
