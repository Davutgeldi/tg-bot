from enum import Enum

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class YesNoAction(Enum):
    yes = "yes"
    no = "no"


class YesNoCallbackData(CallbackData, prefix="music_submit_action"):
    action: YesNoAction


def build_yes_no_inline_kb() -> InlineKeyboardMarkup:
    button_yes = InlineKeyboardButton(
        text="Оформить ✅ ",
        callback_data=YesNoCallbackData(action=YesNoAction.yes).pack(),
    )

    button_no = InlineKeyboardButton(
        text="Отменить ❌ ",
        callback_data=YesNoCallbackData(action=YesNoAction.no).pack(),
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_yes, button_no],
        ]
    )

    return markup