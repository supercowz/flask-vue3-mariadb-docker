"""initial app

Revision ID: 6c2d40dff21c
Revises: 
Create Date: 2024-06-15 22:07:38.128447

"""
import os
from dotenv import find_dotenv, load_dotenv
from database import db, UserModel

# revision identifiers, used by Alembic.
revision = '6c2d40dff21c'
down_revision = None
branch_labels = None
depends_on = None

dot_env = find_dotenv()
if dot_env:
    load_dotenv(dot_env)

def upgrade():
    db.create_all()

    ADMIN_USER = os.environ.get("INITIAL_ADMIN_USER")
    ADMIN_PASSWORD = os.environ.get("INITIAL_ADMIN_USER")
    admin = UserModel(username=ADMIN_USER, password=ADMIN_PASSWORD)
    db.session.add(admin)
    db.session.commit()

def downgrade():
    db.drop_all()