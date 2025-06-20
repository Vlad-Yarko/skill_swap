"""empty message

Revision ID: ec885709d6c1
Revises: fd6c1f8aabf8
Create Date: 2025-06-19 23:31:46.387804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ec885709d6c1'
down_revision: Union[str, None] = 'fd6c1f8aabf8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_exchanges_id', table_name='exchanges')
    op.drop_table('exchanges')
    op.drop_index('ix_skills_category', table_name='skills')
    op.drop_index('ix_skills_title', table_name='skills')
    op.create_index(op.f('ix_skills_title'), 'skills', ['title'], unique=True)
    op.drop_column('skills', 'category')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('skills', sa.Column('category', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_skills_title'), table_name='skills')
    op.create_index('ix_skills_title', 'skills', ['title'], unique=False)
    op.create_index('ix_skills_category', 'skills', ['category'], unique=False)
    op.create_table('exchanges',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('sender_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('receiver_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('skill_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('pending', 'accepted', 'rejected', 'completed', 'cancelled', name='exchangestatus'), autoincrement=False, nullable=True),
    sa.Column('hours_proposed', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], name='exchanges_receiver_id_fkey'),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], name='exchanges_sender_id_fkey'),
    sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], name='exchanges_skill_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='exchanges_pkey')
    )
    op.create_index('ix_exchanges_id', 'exchanges', ['id'], unique=False)
    # ### end Alembic commands ###
