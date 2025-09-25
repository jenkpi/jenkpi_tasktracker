from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import Settings

settings = Settings()
engine = create_async_engine(f"{settings.get_url_string()}")

new_session = async_sessionmaker(engine)
