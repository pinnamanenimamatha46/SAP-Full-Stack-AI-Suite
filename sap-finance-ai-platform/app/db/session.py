from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine_options: dict[str, object] = {
    "pool_pre_ping": True,
}

if settings.database_url.startswith("sqlite"):
    engine_options["connect_args"] = {
        "check_same_thread": False,
    }
else:
    engine_options["connect_args"] = {
        "connect_timeout": 5,
    }

engine = create_engine(
    settings.database_url,
    **engine_options,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
