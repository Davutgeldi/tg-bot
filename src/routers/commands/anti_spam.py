from aiogram import types, Router, F

from src.messages.base_texts import BotMessages

router = Router(name="anti_spam")


@router.message(~F.state)
async def anti_spam_handler(
    message: types.Message,
):
    await message.delete()
    await message.answer(BotMessages.SPAM_TEXT)