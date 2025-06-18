from enum import Enum

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class YesNoAction(Enum):
    yes = "yes"
    no = "no"
    back = "back"


class YesNoCallbackData(CallbackData, prefix="other_yes_no"):
    action: YesNoAction


def build_yes_no_inline_kb() -> InlineKeyboardMarkup:
    button_yes = InlineKeyboardButton(
        text="✅ Оформить",
        callback_data=YesNoCallbackData(action=YesNoAction.yes).pack()
    )

    button_no = InlineKeyboardButton(
        text="❌ Отменить",
        callback_data=YesNoCallbackData(action=YesNoAction.no).pack()
    )

    button_back = InlineKeyboardButton(
        text="🔙 Назад",
        callback_data=YesNoCallbackData(action=YesNoAction.back).pack()
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_yes],
            [button_no],
            [button_back],
        ]
    )

    return markup