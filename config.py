import os

from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")


config = Config()