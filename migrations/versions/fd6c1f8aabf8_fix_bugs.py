"""fix-bugs

Revision ID: fd6c1f8aabf8
Revises: b1744ff7eef6
Create Date: 2025-06-19 22:57:56.604414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'fd6c1f8aabf8'
down_revision: Union[str, None] = 'b1744ff7eef6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_reviews_id', table_name='reviews')
    op.drop_table('reviews')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('exchange_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('reviewer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('reviewed_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['exchange_id'], ['exchanges.id'], name='reviews_exchange_id_fkey'),
    sa.ForeignKeyConstraint(['reviewed_id'], ['users.id'], name='reviews_reviewed_id_fkey'),
    sa.ForeignKeyConstraint(['reviewer_id'], ['users.id'], name='reviews_reviewer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    op.create_index('ix_reviews_id', 'reviews', ['id'], unique=False)
    # ### end Alembic commands ###
