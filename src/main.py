import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.config import settings
from src.routers.commands.base_commands import router as base_commands_router
from src.routers.commands.user_commands import router as user_commands_router
from src.routers.request_handlers.spotify_handler import router as request_handlers_router
from src.routers.request_handlers.telegram_handler import router as telegram_handler_router
from src.routers.request_handlers.other_handler import router as other_handler_router
from src.routers.request_handlers.music_handler import router as music_handler_router
from src.routers.commands.anti_spam import router as anti_spam_router


async def main():
    dp = Dispatcher()

    dp.include_router(base_commands_router)
    dp.include_router(user_commands_router)
    dp.include_router(request_handlers_router)
    dp.include_router(telegram_handler_router)
    dp.include_router(other_handler_router)
    dp.include_router(music_handler_router)
    dp.include_router(anti_spam_router)

    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
