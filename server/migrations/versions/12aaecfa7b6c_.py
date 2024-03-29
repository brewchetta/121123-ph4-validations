"""empty message

Revision ID: 12aaecfa7b6c
Revises: 
Create Date: 2024-02-26 10:37:27.079417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12aaecfa7b6c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('islands_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('square_miles', sa.Integer(), nullable=True),
    sa.Column('average_temperature', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('travelers_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.Column('frequent_flyer', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vacations_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('traveler_id', sa.Integer(), nullable=True),
    sa.Column('island_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['island_id'], ['islands_table.id'], name=op.f('fk_vacations_table_island_id_islands_table')),
    sa.ForeignKeyConstraint(['traveler_id'], ['travelers_table.id'], name=op.f('fk_vacations_table_traveler_id_travelers_table')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacations_table')
    op.drop_table('travelers_table')
    op.drop_table('islands_table')
    # ### end Alembic commands ###
