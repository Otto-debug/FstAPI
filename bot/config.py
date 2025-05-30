import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = 'token'
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://myuser:mypassword@5432/postgres/mydb")

