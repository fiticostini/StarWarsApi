"""empty message

Revision ID: 98e4c106a894
Revises: 41af650894d1
Create Date: 2023-04-21 19:37:24.103073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98e4c106a894'
down_revision = '41af650894d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('eye_color', sa.String(length=15), nullable=True),
    sa.Column('hair_color', sa.String(length=15), nullable=True),
    sa.Column('home_world', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('height', sa.String(length=20), nullable=True),
    sa.Column('weight', sa.String(length=20), nullable=True),
    sa.Column('skin_color', sa.String(length=20), nullable=True),
    sa.Column('date_of_birth', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=60), nullable=False),
    sa.Column('orbital_period', sa.String(length=50), nullable=True),
    sa.Column('rotation_period', sa.String(length=50), nullable=True),
    sa.Column('diameter', sa.String(length=60), nullable=True),
    sa.Column('climate', sa.String(length=80), nullable=True),
    sa.Column('land', sa.String(length=80), nullable=True),
    sa.Column('gravity', sa.String(length=120), nullable=True),
    sa.Column('population', sa.String(length=100), nullable=True),
    sa.Column('species_that_inhabit_the_planet', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
