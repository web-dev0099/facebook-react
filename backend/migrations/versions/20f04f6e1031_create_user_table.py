"""create user table

Revision ID: 20f04f6e1031
Revises: 
Create Date: 2023-01-31 14:46:45.457152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20f04f6e1031'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('subtitle', sa.String(length=255), nullable=False),
    sa.Column('date', sa.String(length=255), nullable=False),
    sa.Column('img', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('post')
    # ### end Alembic commands ###