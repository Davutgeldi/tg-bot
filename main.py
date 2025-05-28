import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.config import settings
from src.routers.commands.base_commands import router as user_commands_router
from src.routers.callback_handlers.services import router as services_router


async def main():
    dp = Dispatcher()

    dp.include_router(user_commands_router)
    dp.include_router(services_router)

    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())