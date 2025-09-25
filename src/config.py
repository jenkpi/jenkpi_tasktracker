from pydantic_settings import BaseSettings
from sqlalchemy import URL


class Settings(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    database: str

    def get_url_string(self) -> str:
        # settings = Settings(_env_prefix="PG_")
        url_string = URL.create(
            "postgresql+asyncpg",
            self.user,
            self.password,
            self.host,
            self.port,
            self.database,
        )
        return url_string
