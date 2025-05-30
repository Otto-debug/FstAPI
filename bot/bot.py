import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config import BOT_TOKEN

from database import get_user_by_telegram_id

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_message(message:Message):
    user = await get_user_by_telegram_id(str(message.from_user.id))
    if user:
        length = len(message.text)
        await message.answer(f"Вы отправили сообщение длиной: {length} символов")
    else:
        await message.answer("Вы не зарегистрированы в системе. Авторизуйтесь через API.")

async def main():
    from database import engine, Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Start poll
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())