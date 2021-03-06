"""empty message

Revision ID: 4f5232f66d6a
Revises: 6ab6b3dcd42c
Create Date: 2017-05-25 05:12:01.449494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f5232f66d6a'
down_revision = '6ab6b3dcd42c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('content', sa.Column('response_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'content', 'response', ['response_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'content', type_='foreignkey')
    op.drop_column('content', 'response_id')
    # ### end Alembic commands ###
