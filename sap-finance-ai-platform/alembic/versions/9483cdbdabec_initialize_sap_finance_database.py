"""Initialize SAP finance database

Revision ID: 9483cdbdabec
Revises:
Create Date: 2026-07-29 16:05:45.979671

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "9483cdbdabec"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
