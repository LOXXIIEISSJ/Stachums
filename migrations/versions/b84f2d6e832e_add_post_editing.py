"""Add post editing

Revision ID: b84f2d6e832e
Revises: 075a7ff32e2f
Create Date: 2022-12-29 22:43:55.862127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b84f2d6e832e'
down_revision = '075a7ff32e2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('edited', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'edited')
    # ### end Alembic commands ###