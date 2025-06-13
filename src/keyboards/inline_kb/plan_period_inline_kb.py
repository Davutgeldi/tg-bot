from enum import Enum

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class SubscriptionPeriod(Enum):
    month = "месяц"
    three_months = "3 месяца"
    six_months = "6 месяцев"
    back = "back"


class SubsPeriodCallbackData(CallbackData, prefix="period"):
    period: SubscriptionPeriod


def build_plan_period_kb() -> InlineKeyboardMarkup:
    button_month = InlineKeyboardButton(
        text="На месяц",
        callback_data=SubsPeriodCallbackData(period=SubscriptionPeriod.month).pack(),
    )

    button_three_months = InlineKeyboardButton(
        text="3 месяца",
        callback_data=SubsPeriodCallbackData(period=SubscriptionPeriod.three_months).pack(),
    )

    button_six_months = InlineKeyboardButton(
        text="6 месяцев",
        callback_data=SubsPeriodCallbackData(period=SubscriptionPeriod.six_months).pack(),
    )

    button_back = InlineKeyboardButton(
        text="⬅️ Назад",
        callback_data=SubsPeriodCallbackData(period=SubscriptionPeriod.back).pack(),
    )

    

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_month],
            [button_three_months],
            [button_six_months],
            [button_back],
        ]
    )

    return markup