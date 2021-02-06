"""insert seed account data

Revision ID: 16cf86d76429
Revises: 950978be0a5f
Create Date: 2021-02-06 05:26:07.949217+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16cf86d76429'
down_revision = '950978be0a5f'
branch_labels = None
depends_on = None


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('account',))
    account_table_tbl = sa.Table('account', meta)

    op.bulk_insert(
        account_table_tbl,
        [
            {
                'login': 'pengsoo',
                'email': 'pengsoo@ebs.com',
                'univ': 'ebs 대학교',
                'profile_nickname': 'EBS의 펭귄 아이돌 펭수',
                'profile_image': 'https://images.chosun.com/resizer/XAPN_U6d8rE0K7b5gdbbrNkfQLI=/616x0/filters:focal(346x272:356x282)/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/HY7VAM77HX3XE6DIXYPZOXAHIU.jpg'
            },
            {
                'login': 'ddookddak',
                'email': 'ddookddak@ebs.com',
                'univ': 'ebs 대학교',
                'profile_nickname': '틀딱이',
                'profile_image': 'http://down.humoruniv.org//hwiparambbs/data/editor/pdswait/e_7954929758_11793b422f85f307eb741dfca09d74758b5b1186.jpg'
            },
        ]
    )


def downgrade():
    pass
