from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    telegram_chat_id: str
    scheduler_interval_hours: int = 1
    scheduler_timezone: str = "UTC"
    defillama_base_url: str = "https://yields.llama.fi"
    log_level: str = "INFO"
    data_dir: str = "./data"

    class Config:
        env_file = ".env"


settings = Settings()

