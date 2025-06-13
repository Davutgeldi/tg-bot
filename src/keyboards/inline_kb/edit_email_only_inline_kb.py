from enum import Enum

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class EmailOnlyAction(Enum):
    edit_email = "edit_email"
    submit = "submit"


class EmailOnlyCallbackData(CallbackData, prefix="email_only"):
    action: EmailOnlyAction


def build_email_only_inline_kb() -> InlineKeyboardMarkup:
    button_edit_email = InlineKeyboardButton(
        text="Изменить Email ✏️",
        callback_data=EmailOnlyCallbackData(action=EmailOnlyAction.edit_email).pack(),
    )

    button_confirm = InlineKeyboardButton(
        text="Подтвердить 📩",
        callback_data=EmailOnlyCallbackData(action=EmailOnlyAction.submit).pack(),
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_edit_email],
            [button_confirm],
        ]
    )

    return markup
