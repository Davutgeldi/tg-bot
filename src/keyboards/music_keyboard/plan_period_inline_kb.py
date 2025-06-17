from enum import Enum

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class PlanPeriod(Enum):
    month = "Месяц"
    year = "Год"
    back = "back"


class PlanPeriodCallbackData(CallbackData, prefix="plan_period"):
    period: PlanPeriod


def build_plan_period_kb() -> InlineKeyboardMarkup:
    button_month = InlineKeyboardButton(
        text="📅 Месяц",
        callback_data=PlanPeriodCallbackData(period=PlanPeriod.month.value).pack()
    )

    button_year = InlineKeyboardButton(
        text="🗓️ Год",
        callback_data=PlanPeriodCallbackData(period=PlanPeriod.year.value).pack(),
    )

    button_back = InlineKeyboardButton(
        text="🔙 Назад",
        callback_data=PlanPeriodCallbackData(period=PlanPeriod.back.value).pack(),
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_month],
            [button_year],
            [button_back],
        ]
    )
    return markup 