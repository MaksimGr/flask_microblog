"""followers

Revision ID: 025f64ff19af
Revises: e80a266eb6da
Create Date: 2020-10-24 23:30:51.689711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '025f64ff19af'
down_revision = 'e80a266eb6da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
