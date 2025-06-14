from enum import Enum

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class TgPlan(Enum):
    month = "Премиум на месяц"
    year = "Премиум на Год"
    stars = "Купить звезды"
    back = "back"


class TgPlanCallbackData(CallbackData, prefix="tg_plan"):
    plan: TgPlan


def build_tg_plan_kb() -> InlineKeyboardMarkup:
    button_month = InlineKeyboardButton(
        text="Премиум на месяц",
        callback_data=TgPlanCallbackData(plan=TgPlan.month).pack(),
    )

    button_year = InlineKeyboardButton(
        text="Премиум на Год",
        callback_data=TgPlanCallbackData(plan=TgPlan.year).pack(),
    )

    button_stars = InlineKeyboardButton(
        text="⭐ Купить звезды",
        callback_data=TgPlanCallbackData(plan=TgPlan.stars).pack(),
    )

    button_back = InlineKeyboardButton(
        text="⬅️ Назад",
        callback_data=TgPlanCallbackData(plan=TgPlan.back).pack(),
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_month],
            [button_year],
            [button_stars],
            [button_back],
        ]
    )

    return markup