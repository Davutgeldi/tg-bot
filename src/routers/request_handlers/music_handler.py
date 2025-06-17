from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from src.config import settings
from src.messages.music_prompts import MusicForms
from src.keyboards.service_inline_kb import ServicesCallbackData, ServiceName
from src.keyboards.music_keyboard.plan_inline_kb import (
    MusicPlanCallbackData,
    MusicPlan,
    build_music_plan_keyboard,
)
from src.keyboards.music_keyboard.plan_period_inline_kb import (
    PlanPeriod,
    PlanPeriodCallbackData,
    build_plan_period_kb,
)
from src.keyboards.music_keyboard.yes_no_inline_kb import (
    YesNoCallbackData, 
    YesNoAction,
    build_yes_no_inline_kb,
)


router = Router(name="music_handler")


@router.callback_query(ServicesCallbackData.filter(F.service == ServiceName.music))
async def handle_music_service(
    callback: types.CallbackQuery,
    callback_data: ServicesCallbackData,
    state: FSMContext,
):
    await state.update_data(service=callback_data.service.value)

    await callback.message.answer(
        text="💡 Выберите подходящий план:",
        reply_markup=build_music_plan_keyboard(),
    )


@router.callback_query(MusicPlanCallbackData.filter(F.plan == MusicPlan.back))
async def handle_back(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await callback.message.delete()
    await state.clear()


@router.callback_query(MusicPlanCallbackData.filter())
async def handle_plan(
    callback: types.CallbackQuery,
    callback_data: MusicPlanCallbackData,
    state: FSMContext,
):
    await callback.message.delete()
    await state.update_data(plan=callback_data.plan.value)

    await callback.message.answer(
        text="📅 Пожалуйста, выберите срок подписки:",
        reply_markup=build_plan_period_kb(),
    )


@router.callback_query(PlanPeriodCallbackData.filter(F.period == PlanPeriod.back))
async def handle_back_to_plan(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await callback.message.delete()
    await callback.message.answer(
        text="💡 Выберите подходящий план:",
        reply_markup=build_music_plan_keyboard(),
    )


@router.callback_query(PlanPeriodCallbackData.filter())
async def handle_plan_period(
    callback: types.CallbackQuery,
    callback_data: PlanPeriodCallbackData,
    state: FSMContext,
):
    await callback.message.delete()

    await state.update_data(period=callback_data.period.value)

    data = await state.get_data()
    username = callback.from_user.username

    await callback.message.answer(
        text=MusicForms.get_request_text(data, username),
        reply_markup=build_yes_no_inline_kb(),
    )


@router.callback_query(YesNoCallbackData.filter(F.action == YesNoAction.yes))
async def handle_yes(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await callback.message.delete()

    data = await state.get_data()
    username = callback.from_user.username

    await callback.message.bot.send_message(
        chat_id=settings.admin_chat_id,
        text=MusicForms.get_request_text(data, username),
    )

    await callback.message.answer(MusicForms.SUCCESS_SUBMIT_TEXT)

    await state.clear()


@router.callback_query(YesNoCallbackData.filter(F.action == YesNoAction.no))
async def handle_no(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await callback.message.delete()
    await callback.message.answer(
        text=MusicForms.CANCELLATION_MESSAGE,
    )

    await state.clear()
