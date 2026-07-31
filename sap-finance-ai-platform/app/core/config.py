from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SAP Finance AI Platform"
    database_url: str = "sqlite+pysqlite:///./sap_finance.db"

    secret_key: str = "change-this-secret-key-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()

## uv run python -c "import secrets; print(secrets.token_urlsafe(64))"

## uv run ruff check app\core\security.py app\core\config.py
## uv run ruff format app\core\security.py app\core\config.py
