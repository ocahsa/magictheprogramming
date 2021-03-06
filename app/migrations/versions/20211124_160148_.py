"""empty message

Revision ID: 995749bffd44
Revises: ffdc0a98111c
Create Date: 2021-11-24 16:01:48.393576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '995749bffd44'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('type_line', sa.String(length=80), nullable=False),
    sa.Column('oracle_text', sa.String(length=4000), nullable=True),
    sa.Column('mana_value', sa.Integer(), nullable=False),
    sa.Column('mana_cost', sa.String(length=40), nullable=True),
    sa.Column('colors', sa.String(length=100), nullable=False),
    sa.Column('image_url', sa.String(length=6000), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('decks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('format', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=10000), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('decklists',
    sa.Column('deck_id', sa.Integer(), nullable=False),
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['cards.id'], ),
    sa.ForeignKeyConstraint(['deck_id'], ['decks.id'], ),
    sa.PrimaryKeyConstraint('deck_id', 'card_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('decklists')
    op.drop_table('decks')
    op.drop_table('cards')
    # ### end Alembic commands ###
