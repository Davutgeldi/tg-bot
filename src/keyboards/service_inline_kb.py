from enum import Enum

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class ServiceName(Enum):
    spotify = "spotify"
    music = "apple music"
    telegram = "telegram_premium"
    other = "other"


class ServicesCallbackData(CallbackData, prefix="service"):
    service: ServiceName


def build_services_kb() -> InlineKeyboardMarkup:
    button_spotify = InlineKeyboardButton(
        text="Spotify",
        callback_data=ServicesCallbackData(service=ServiceName.spotify).pack(),
    )

    button_apple_music = InlineKeyboardButton(
        text="Apple Music",
        callback_data=ServicesCallbackData(
            service=ServiceName.music,
        ).pack(),
    )

    button_tg_premium = InlineKeyboardButton(
        text="Telegram Premium",
        callback_data=ServicesCallbackData(
            service=ServiceName.telegram,
        ).pack(),
    )

    button_other = InlineKeyboardButton(
        text="Другое",
        callback_data=ServicesCallbackData(
            service=ServiceName.other,
        ).pack(),
    )
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_spotify, button_apple_music],
            [button_tg_premium, button_other],
        ]
    )

    return markup
