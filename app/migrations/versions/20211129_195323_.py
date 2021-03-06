"""empty message

Revision ID: f218a2cf80d8
Revises: e1559cae1bfe
Create Date: 2021-11-29 19:53:23.876309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f218a2cf80d8'
down_revision = 'e1559cae1bfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards', sa.Column('art_crop', sa.String(length=6000), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cards', 'art_crop')
    # ### end Alembic commands ###
