"""empty message

Revision ID: bcc82a7dcc31
Revises: c4f058e59bf1
Create Date: 2017-05-14 13:44:44.698700

"""

# revision identifiers, used by Alembic.
revision = 'bcc82a7dcc31'
down_revision = 'c4f058e59bf1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_to_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=True),
    sa.Column('labels', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image_to_text')
    ### end Alembic commands ###
