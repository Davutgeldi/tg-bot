import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from config import config


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}")


@dp.message(Command(commands=["help", "pomogi"]))
async def handle_help(message: types.Message):
    await message.answer("This is help message")


@dp.message()
async def answer(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Emin cmo",
    )
    await message.answer(text=message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())