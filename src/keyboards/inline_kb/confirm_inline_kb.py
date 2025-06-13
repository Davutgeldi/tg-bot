from enum import Enum

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class EditAction(Enum):
    email = "email"
    password = "password"


class ReviewAction(Enum):
    edit = "edit"
    submit = "submit"


class EditActionCallbackData(CallbackData, prefix="edit_action"):
    action: EditAction


class ReviewActionCallbackData(CallbackData, prefix="review_action"):
    action: ReviewAction


def build_confirm_inline_kb() -> InlineKeyboardMarkup:
    button_edit = InlineKeyboardButton(
        text="✏️ Изменить",
        callback_data=ReviewActionCallbackData(action=ReviewAction.edit).pack(),
    )

    button_submit = InlineKeyboardButton(
        text="✅ Подтвердить",
        callback_data=ReviewActionCallbackData(action=ReviewAction.submit).pack(),
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_edit],
            [button_submit],
        ]
    )

    return markup


def build_edit_data_inline_kb() -> InlineKeyboardMarkup:
    button_email = InlineKeyboardButton(
        text="✉️ Изменить Email",
        callback_data=EditActionCallbackData(action=EditAction.email).pack(),
    )

    button_password = InlineKeyboardButton(
        text="🔑 Изменить Пароль",
        callback_data=EditActionCallbackData(action=EditAction.password).pack(),
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_email],
            [button_password],
        ]
    )

    return markup
