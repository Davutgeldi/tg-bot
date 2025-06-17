from enum import Enum

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class MusicPlan(Enum):
    individual = "Индивидуальный"
    family = "Семейный"
    back = "back"


class MusicPlanCallbackData(CallbackData, prefix="music_plan"):
    plan: MusicPlan


def build_music_plan_keyboard() -> InlineKeyboardMarkup:
    button_individual = InlineKeyboardButton(
        text="🎵 Индивидуальный",
        callback_data=MusicPlanCallbackData(plan=MusicPlan.individual).pack(),
    )

    button_family = InlineKeyboardButton(
        text="👨‍👩‍👧‍👦 Семейный",
        callback_data=MusicPlanCallbackData(plan=MusicPlan.family).pack(),
    )

    button_back = InlineKeyboardButton(
        text="⬅️ Назад",
        callback_data=MusicPlanCallbackData(plan=MusicPlan.back).pack(),
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button_individual],
            [button_family],
            [button_back],
        ],
    )
    
    return markup