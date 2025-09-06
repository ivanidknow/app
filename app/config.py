from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    APP_NAME: str = Field(default="service-1")
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)

    DATABASE_URL: str = Field(default="postgresql+asyncpg://app:app@postgres:5432/appdb")
    REDIS_URL: str = Field(default="redis://redis:6379/0")

    METRICS_ENABLED: bool = Field(default=True)

settings = Settings()