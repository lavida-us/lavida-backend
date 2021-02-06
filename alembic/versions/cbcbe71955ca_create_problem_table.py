"""create problem table

Revision ID: cbcbe71955ca
Revises: ce25cb1d2949
Create Date: 2021-02-06 03:25:55.141626+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbcbe71955ca'
down_revision = 'ce25cb1d2949'
branch_labels = None
depends_on = None

class Writer(sa.types.UserDefinedType):
    def get_col_spec(self, **kw):
        return "Writer"

    def bind_processor(self, dialect):
        def process(value):
            return value
        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            return value
        return process

def upgrade():
    op.create_table(
        'problem',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(128), nullable=False),
        sa.Column('writers', sa.types.ARRAY(sa.JSON)),
        sa.Column('editors', sa.types.ARRAY(sa.JSON)),
        sa.Column('source_name', sa.String),
        sa.Column('source_url', sa.String),
    )


def downgrade():
    op.drop_table('problem')
