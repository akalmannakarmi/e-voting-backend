from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "vote-service"
    database_url: str

    jwt_secret: str
    jwt_algorithm: str = "HS256"

    ballot_service_url: str

    class Config:
        env_file = ".env"


settings = Settings()
