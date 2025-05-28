from aiogram import F, Router
from aiogram.types import CallbackQuery

from src.keyboards.inline_kb import ServiceName, ServicesCallbackData


router = Router(name="services_router")


@router.callback_query(
    ServicesCallbackData.filter(F.service == ServiceName.spotify)
)
async def handle_spotify_service(callback_query: CallbackQuery):
    await callback_query.message.answer(
        text="Спотифай выбрали скиньте логин и пароль",
    )