"""empty message

Revision ID: f40e963c747f
Revises: 1e909f130f74
Create Date: 2024-05-13 14:44:38.260864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f40e963c747f'
down_revision = '1e909f130f74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('under_sea_house_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('house_type', sa.String(), nullable=False),
    sa.Column('comfortable', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('under_sea_house_table')
    # ### end Alembic commands ###
