from aiogram import F, Router, types

from src.messages.base_texts import BotMessages
from src.keyboards.reply_kb import ButtonText


router = Router(name="user_commands")


@router.message(F.text == ButtonText.SUPPORT)
async def handle_support(message: types.Message):
    await message.answer(text=BotMessages.SUPPORT)
