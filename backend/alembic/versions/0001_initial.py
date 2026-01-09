"""initial

Revision ID: 0001_initial
Revises: 
Create Date: 2025-11-17 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(length=256), nullable=False, unique=True),
        sa.Column('full_name', sa.String(length=256), nullable=True),
        sa.Column('hashed_password', sa.String(length=512), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True, server_default=sa.text('true')),
        sa.Column('is_superuser', sa.Boolean(), nullable=True, server_default=sa.text('false')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'))
    )

    op.create_table(
        'master_profiles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('title', sa.String(length=256), nullable=True),
        sa.Column('summary', sa.Text(), nullable=True),
        sa.Column('data', postgresql.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'))
    )

    op.create_table(
        'resume_snippets',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('profile_id', sa.Integer(), sa.ForeignKey('master_profiles.id', ondelete='CASCADE'), nullable=False),
        sa.Column('section', sa.String(length=128), nullable=False),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('tags', postgresql.JSON(), nullable=True),
        sa.Column('embedding_id', sa.String(length=256), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'))
    )

def downgrade():
    op.drop_table('resume_snippets')
    op.drop_table('master_profiles')
    op.drop_table('users')
