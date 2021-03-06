"""empty message

Revision ID: 12cb4912b033
Revises: 213a30c7cb68
Create Date: 2021-12-03 01:31:29.940028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12cb4912b033'
down_revision = '213a30c7cb68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards', sa.Column('name', sa.String(length=3000), nullable=False))
    op.add_column('cards', sa.Column('mana_cost', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cards', 'mana_cost')
    op.drop_column('cards', 'name')
    # ### end Alembic commands ###
