from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command

from src.keyboards.reply_kb import ButtonText, get_on_start_kb
from src.keyboards.service_inline_kb import build_services_kb
from src.messages.base_texts import BotMessages


router = Router(name="base_commands_router")


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text=BotMessages.START,
        reply_markup=get_on_start_kb(),
    )

    await message.answer(BotMessages.BOT_RULES)
    
    await message.answer(
        text=BotMessages.BUTTON,
        reply_markup=build_services_kb(),
    )


@router.message(F.text == ButtonText.HELP)
@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(BotMessages.HELP)
