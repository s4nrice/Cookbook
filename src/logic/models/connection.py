from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from logic import settings


class PostgresConnection:
    """Postgres`s connection class"""

    DATABASE_URL = (
        f"postgresql+asyncpg://{settings.postgres_username}:"
        f"{settings.postgres_password}@{settings.postgres_host}:"
        f"{settings.postgres_port}/{settings.postgres_database}"
    )
    # DATABASE_URL = (
    #     f"postgresql+asyncpg://postgres:"
    #     f"postgres@localhost:"
    #     f"5433/postgres"
    # )

    engine = create_async_engine(DATABASE_URL)
    local_session = async_sessionmaker(engine, expire_on_commit=False)

    @classmethod
    async def get_db(cls) -> AsyncGenerator[AsyncSession, None]:
        async with cls.local_session() as session:
            yield session
