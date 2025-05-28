from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ButtonText:
    HELP: str = "❓ Как пользоваться ботом ?"
    SUPPORT: str = "👨‍💻 Связаться с поддержкой"


def get_on_start_kb() -> ReplyKeyboardMarkup:
    button_help = KeyboardButton(text=ButtonText.HELP)
    button_support = KeyboardButton(text=ButtonText.SUPPORT)

    buttons_first_row = [button_help]
    buttons_second_row = [button_support]
    markup = ReplyKeyboardMarkup(
        keyboard=[buttons_first_row, buttons_second_row],
        resize_keyboard=True,
    )

    return markup
