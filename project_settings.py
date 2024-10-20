import os
from dotenv import load_dotenv
import ast

load_dotenv()


def getenv(name, default=None):
    obj = os.getenv(name, default)
    if isinstance(obj, list):
        return ast.literal_eval(obj)
    return obj


BOT_TOKEN = getenv("BOT_TOKEN")

DB_HOST: str = getenv("DB_HOST", "localhost")
DB_PORT: int = getenv("DB_PORT", 5432)
DB_NAME: str = getenv("DB_NAME", "tg_constructor")
DB_USERNAME: str = getenv("DB_USERNAME", "tg_constructor")
DB_PASSWORD: str = getenv("DB_PASSWORD", "123")
