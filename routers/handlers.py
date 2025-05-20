from aiogram import Router, types
from aiogram.enums import ChatAction


router = Router(name="handlers_router")


@router.message()
async def echo_handler(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )
    await message.copy_to(
        chat_id=message.chat.id,
        text=f"{message.text}",
    )
    await message.answer("data was sent")