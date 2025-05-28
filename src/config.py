from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    bot_token: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()