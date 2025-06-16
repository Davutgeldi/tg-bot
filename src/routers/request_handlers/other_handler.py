from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from src.config import settings
from src.messages.other_prompts import OtherForms
from src.keyboards.service_inline_kb import ServicesCallbackData, ServiceName


router = Router(name="other_handler")


@router.callback_query(ServicesCallbackData.filter(F.service == ServiceName.other))
async def handle_other_service(
    callback: types.CallbackQuery,
    callback_data: ServicesCallbackData,
):
    service = callback_data.service.value
    username = callback.from_user.username
    await callback.message.bot.send_message(
        chat_id=settings.admin_chat_id,
        text=OtherForms.get_request_text(service, username),
    )

    await callback.message.answer(OtherForms.SUCCESS_SUBMIT_TEXT)
    
    