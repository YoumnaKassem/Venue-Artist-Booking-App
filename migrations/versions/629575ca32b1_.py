"""empty message

Revision ID: 629575ca32b1
Revises: d1bebc9e3875
Create Date: 2020-10-25 15:47:07.020996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '629575ca32b1'
down_revision = 'd1bebc9e3875'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('address', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'address')
    # ### end Alembic commands ###
