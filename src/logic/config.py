import os
from typing import Any

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(".env")

if os.path.exists(".env.local"):
    load_dotenv(".env.local", override=True)


class Settings(BaseModel):
    """Project configuration class."""

    # Postgres
    postgres_username: str
    postgres_password: str
    postgres_database: str
    postgres_host: str
    postgres_port: int

    class Config:
        frozen = True


def get_config() -> Settings:
    """Get a config instance."""
    # __config_params: dict[str, Any] = {
    #     param: os.environ.get(param.upper()) for param in Settings.model_fields
    # }

    # return Settings(**__config_params)
    return Settings(
        postgres_user=os.getenv("POSTGRES_USER"),
        postgres_password=os.getenv("POSTGRES_PASSWORD"),
        postgres_db=os.getenv("POSTGRES_DB"),
        postgres_host=os.getenv("POSTGRES_HOST"),
        postgres_port=int(os.getenv("POSTGRES_PORT")),
    )
