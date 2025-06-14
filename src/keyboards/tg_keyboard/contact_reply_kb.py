from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def share_contact_kb() -> ReplyKeyboardMarkup:
    contact = KeyboardButton(
        text="📱 Поделиться контактом",
        request_contact=True,
    )

    return ReplyKeyboardMarkup(
        keyboard=[[contact]],
        resize_keyboard=True,
        one_time_keyboard=True,
    )