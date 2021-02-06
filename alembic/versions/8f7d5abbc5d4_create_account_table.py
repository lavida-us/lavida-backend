"""create account table

Revision ID: 8f7d5abbc5d4
Revises: 
Create Date: 2021-02-06 03:02:18.794976+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f7d5abbc5d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('login', sa.String(128), nullable=False),
        sa.Column('email', sa.String(128)),
        sa.Column('univ', sa.String(128)),
        sa.Column('profile_nickname', sa.String(128)),
        sa.Column('profile_image', sa.String(65536)),
    )


def downgrade():
    op.drop_table('account')
