from enum import Enum 

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class SubscriptionPlan(Enum):
    individual = "Индивидуальный"
    duo = "Дуо (для двоих)"
    family = "Семейный (6 человек)"


class SubscriptionCallbackData(CallbackData, prefix="subscription"):
    plan: SubscriptionPlan


def build_subscription_kb() -> InlineKeyboardMarkup:
    button_individual = InlineKeyboardButton(
        text="Индивидуальный",
        callback_data=SubscriptionCallbackData(plan=SubscriptionPlan.individual).pack(),
    )

    button_duo = InlineKeyboardButton(
        text="Дуо (для двоих)",
        callback_data=SubscriptionCallbackData(plan=SubscriptionPlan.duo).pack(),
    )

    button_family = InlineKeyboardButton(
        text="Семейный (6 человек)",
        callback_data=SubscriptionCallbackData(plan=SubscriptionPlan.family).pack(),
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_individual],
            [button_duo],
            [button_family],
        ],
    )

    return markup