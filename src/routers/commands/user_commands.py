from aiogram import F, Router, types
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.messages.base_texts import BotMessages
from src.keyboards.reply_kb import ButtonText
from src.keyboards.service_inline_kb import build_services_kb


router = Router(name="user_commands")


@router.message(F.text == ButtonText.SUPPORT)
async def handle_support(message: types.Message):
    await message.answer(text=BotMessages.SUPPORT)


@router.message(Command("stop"))
async def handle_stop(
    message: types.Message,
    state: FSMContext,
):
    await state.clear()
    await message.delete()
    await message.answer(text=BotMessages.CANCEL_TEXT, reply_markup=ReplyKeyboardRemove())


@router.message(Command("service"))
async def handle_service(
    message: types.Message,
):
    await message.answer(
        text=BotMessages.BUTTON,
        reply_markup=build_services_kb(),
    )


@router.message(Command("rules"))
async def handle_rules(
    message: types.Message,
):
    await message.answer(text=BotMessages.BOT_RULES)