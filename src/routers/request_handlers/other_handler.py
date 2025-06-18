from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from src.config import settings
from src.messages.other_prompts import OtherForms
from src.keyboards.service_inline_kb import ServicesCallbackData, ServiceName
from src.keyboards.other_keyboard.yes_no_inline_kb import (
    YesNoAction,
    YesNoCallbackData,
    build_yes_no_inline_kb,
)


router = Router(name="other_handler")


@router.callback_query(ServicesCallbackData.filter(F.service == ServiceName.other))
async def handle_other_service(
    callback: types.CallbackQuery,
    callback_data: ServicesCallbackData,
    state: FSMContext,
):
    await state.update_data(service=callback_data.service.value)

    await callback.message.answer(
        text=OtherForms.OTHER_SERVICES_TEXT,
        reply_markup=build_yes_no_inline_kb(),
    )    
    

@router.callback_query(YesNoCallbackData.filter(F.action == YesNoAction.back))
async def handle_other_back(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await state.clear()

    await callback.message.delete()


@router.callback_query(YesNoCallbackData.filter(F.action == YesNoAction.no))
async def handle_other_no(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await state.clear()

    await callback.message.delete()


@router.callback_query(YesNoCallbackData.filter(F.action == YesNoAction.yes))
async def handle_other_yes(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    data = await state.get_data()
    service = data.get("service")
    username = callback.from_user.username

    await callback.message.delete()

    await callback.bot.send_message(
        chat_id=settings.admin_chat_id,
        text=OtherForms.get_request_text(service, username)
    )

    await callback.message.answer(OtherForms.SUCCESS_SUBMIT_TEXT)

    await state.clear()