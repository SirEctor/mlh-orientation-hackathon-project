"""empty message

Revision ID: 09c1f59f2618
Revises: 
Create Date: 2021-07-03 21:26:55.222195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "09c1f59f2618"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
