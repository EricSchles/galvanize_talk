"""empty message

Revision ID: 75a9a634acd6
Revises: b9fabcf684b6
Create Date: 2017-05-13 13:50:02.600428

"""

# revision identifiers, used by Alembic.
revision = '75a9a634acd6'
down_revision = 'b9fabcf684b6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ad_info', sa.Column('city', sa.String(), nullable=True))
    op.add_column('ad_info', sa.Column('state', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ad_info', 'state')
    op.drop_column('ad_info', 'city')
    ### end Alembic commands ###
