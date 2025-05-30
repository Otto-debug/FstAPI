from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import select
from sqlalchemy import Column, Integer, String

from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    password_hash = Column(String)
    telegram_id = Column(String, nullable=True)

async def get_user_by_telegram_id(telegram_id: str):
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.telegram_id == telegram_id))
        return result.scalar_one_or_none()
    
