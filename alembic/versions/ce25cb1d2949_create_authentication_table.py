"""create authentication table

Revision ID: ce25cb1d2949
Revises: 8f7d5abbc5d4
Create Date: 2021-02-06 03:11:51.013909+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce25cb1d2949'
down_revision = '8f7d5abbc5d4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'authentication',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('account_id', sa.Integer, sa.ForeignKey('account.id')),
        sa.Column('hashed_password', sa.String)
    )


def downgrade():
    op.drop_table('authentication')
