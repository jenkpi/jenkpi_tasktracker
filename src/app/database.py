from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import PgSettings

settings = PgSettings(_env_prefix="PG_")  # type: ignore[call-arg]
engine = create_async_engine(settings.get_url_string())

new_session = async_sessionmaker(engine)
