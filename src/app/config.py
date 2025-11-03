from pydantic_settings import BaseSettings
from sqlalchemy import URL


class PgSettings(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    database: str

    def get_url_string(self) -> URL:
        # settings = Settings(_env_prefix="PG_")
        print(self)
        url_string = URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password="pass",
            host=self.host,
            port=self.port,
            database=self.database,
        )
        print(url_string)
        return url_string


class KafkaSettings(BaseSettings):
    socket: str
    topic: str
