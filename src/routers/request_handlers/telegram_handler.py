from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.config import settings
from src.keyboards.service_inline_kb import ServicesCallbackData, ServiceName
from src.keyboards.tg_keyboard.plan_inline_kb import (
    build_tg_plan_kb,
    TgPlanCallbackData,
    TgPlan,
)
from src.keyboards.tg_keyboard.contact_reply_kb import share_contact_kb
from src.states.tg_states import Request
from src.messages.tg_prompts import TgForms


router = Router(name="tg_premium_handler")


@router.callback_query(ServicesCallbackData.filter(F.service == ServiceName.telegram))
async def handle_service_selection(
    callback: types.CallbackQuery,
    callback_data: ServicesCallbackData,
    state: FSMContext,
):
    await state.update_data(service=callback_data.service.value)

    await callback.message.answer(
        text="⭐ Выберите тариф Telegram Premium:",
       reply_markup=build_tg_plan_kb(),
    )
    

@router.callback_query(TgPlanCallbackData.filter(F.plan == TgPlan.back))
async def handle_back(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await callback.message.delete()
    await state.clear()


@router.callback_query(TgPlanCallbackData.filter(F.plan == TgPlan.month))
async def handle_month_plan(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await state.update_data(plan=TgPlan.month.value)

    await callback.message.delete()

    await callback.message.answer(text=TgForms.NUMBER_PROMPT, reply_markup=share_contact_kb())
    await state.set_state(Request.contact)


@router.callback_query(TgPlanCallbackData.filter(F.plan == TgPlan.year))
async def handle_year_plan(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await state.update_data(plan=TgPlan.year.value)

    await callback.message.delete()

    await callback.message.answer(text=TgForms.NUMBER_PROMPT, reply_markup=share_contact_kb())
    await state.set_state(Request.contact)


@router.message(Request.contact)
async def handle_number(
    message: types.Message,
    state: FSMContext,
):
    username = message.from_user.username
    
    if message.contact:
        phone_number = message.contact.phone_number
        await state.update_data(contact=phone_number)

        await message.answer(TgForms.CONFIRMATION_TEXT, reply_markup=ReplyKeyboardRemove())
        
        await message.bot.send_message(
            chat_id=settings.admin_chat_id,
            text=TgForms.get_request_text(phone_number, username)
        )
        await message.delete()
        return
    
    await message.answer(TgForms.USE_REPLY_BUTTON, reply_markup=share_contact_kb())