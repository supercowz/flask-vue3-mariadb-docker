"""initial app

Revision ID: 6c2d40dff21c
Revises: 
Create Date: 2024-06-15 22:07:38.128447

"""
from alembic import op
import sqlalchemy as sa
from database import db


# revision identifiers, used by Alembic.
revision = '6c2d40dff21c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    db.create_all()

def downgrade():
    db.drop_all()