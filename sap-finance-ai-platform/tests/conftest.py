import pytest

from app.db.base import Base
from app.db.session import engine
from app.models.finance_analysis import FinanceAnalysis  # noqa: F401


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """Create SQLite tables before tests and remove them afterward."""
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)
