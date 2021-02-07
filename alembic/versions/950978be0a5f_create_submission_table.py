"""create submission table

Revision ID: 950978be0a5f
Revises: cbcbe71955ca
Create Date: 2021-02-06 04:44:32.808928+00:00

"""
from alembic import op
import sqlalchemy as sa
import enum

# revision identifiers, used by Alembic.
revision = '950978be0a5f'
down_revision = 'cbcbe71955ca'
branch_labels = None
depends_on = None

class Status(enum.Enum):
    pending = 1
    judging = 2
    judged = 3

class Result(enum.Enum):
    accept = 1
    wrong_answer = 2
    time_limit_exceed = 3
    memory_limit_exceed = 4
    compile_error = 5
    runtime_error = 6

def upgrade():
    op.create_table(
        'submission',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('owned_account_id', sa.Integer, sa.ForeignKey('account.id'), nullable=False),
        sa.Column('problem_id', sa.Integer, sa.ForeignKey('problem.id'), nullable=False),
        sa.Column('status', sa.Enum(Status, name="status_type", create_type=False), nullable=False),
        sa.Column('result', sa.Enum(Result, name="result_type", create_type=False)),
        sa.Column('time', sa.Float),
        sa.Column('memory', sa.Float),
        sa.Column('programming_language', sa.String),
    )


def downgrade():
    op.execute('DROP TYPE result_type CASCADE')
    op.execute('DROP TYPE status_type CASCADE')
    op.drop_table('submission')
