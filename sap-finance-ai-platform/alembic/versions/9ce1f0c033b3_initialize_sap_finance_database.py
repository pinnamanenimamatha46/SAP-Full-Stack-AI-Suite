"""Initialize SAP finance database

Revision ID: 9ce1f0c033b3
Revises: 9483cdbdabec
Create Date: 2026-07-29 16:06:49.886700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ce1f0c033b3'
down_revision: Union[str, Sequence[str], None] = '9483cdbdabec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
