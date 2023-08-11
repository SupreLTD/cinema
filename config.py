from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: SecretStr

    model_config = SettingsConfigDict(env_file=".env")


config = Settings()
