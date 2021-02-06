"""insert seed problem data

Revision ID: f37115dce4c2
Revises: 16cf86d76429
Create Date: 2021-02-06 05:42:18.478461+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f37115dce4c2'
down_revision = '16cf86d76429'
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('problem',))
    problem_table_tbl = sa.Table('problem', meta)

    op.bulk_insert(
        problem_table_tbl,
        [
            {
                'title': '아름다운 만영로',
                'writers': [
                    {'name': '한만영', 'email': '한만영@이메일.com', 'homepage': 'https://만영홈페이지.com'},
                ],
                'editors': [
                    {'name': 'X준X', 'email': 'X준X@이메일.com', 'homepage': 'https://X준X홈페이지.com'},
                    {'name': '김XX', 'email': '김XX@이메일.com', 'homepage': 'https://김XX홈페이지.com'},
                ],
                'source_name': '2019 아주대학교 프로그래밍 경시대회 APC - Div.1',
                'source_url': None,
            },
            {
                'title': '금광',
                'writers': [],
                'editors': [],
                'source_name': 'KOI 2014 중등부',
                'source_url': 'https://koi.or.kr/',
            },
        ]
    )


def downgrade():
    pass
