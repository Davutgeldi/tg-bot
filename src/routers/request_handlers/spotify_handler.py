from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from email_validator import validate_email, EmailNotValidError


from src.keyboards.service_inline_kb import ServicesCallbackData, ServiceName
from src.keyboards.spotify_keyboard.yes_no_inline_kb import YesNoAction, YesNoCallbackData, build_yes_no_inline_kb
from src.keyboards.service_inline_kb import build_services_kb
from src.keyboards.spotify_keyboard.edit_email_only_inline_kb import (
    EmailOnlyAction, 
    EmailOnlyCallbackData, 
    build_email_only_inline_kb
)
from src.keyboards.spotify_keyboard.subscription_inline_kb import (
    build_subscription_kb,
    SubscriptionCallbackData,
    SubscriptionPlan,
)
from src.keyboards.spotify_keyboard.plan_period_inline_kb import (
    SubsPeriodCallbackData,
    SubscriptionPeriod,
    build_plan_period_kb,
)
from src.keyboards.spotify_keyboard.confirm_inline_kb import (
    build_confirm_inline_kb, 
    build_edit_data_inline_kb, 
    ReviewActionCallbackData,
    EditActionCallbackData,
    EditAction,
    ReviewAction,
)
from src.states.spotify_states import Request
from src.config import settings
from src.messages.spotify_prompts import ServiceForms
from src.messages.base_texts import BotMessages


router = Router(name="request_handlers")


@router.callback_query(ServicesCallbackData.filter(F.service == ServiceName.spotify))
async def handle_service_selection(
    callback: types.CallbackQuery,
    callback_data: ServicesCallbackData,
    state: FSMContext,
):
    await state.update_data(service=callback_data.service.value)

    await callback.message.answer(
        text="У вас уже есть подписка на Spotify?",
        reply_markup=build_yes_no_inline_kb(),
    )


@router.callback_query(YesNoCallbackData.filter(F.action == YesNoAction.back))
async def handle_back(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await callback.message.delete()
    await state.clear()
    await callback.message.edit_text(
        text=BotMessages.BUTTON,
        reply_markup=build_services_kb(),
    )
    
    
@router.callback_query(YesNoCallbackData.filter(F.action == YesNoAction.yes))
async def handle_yes(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await callback.message.delete()

    await callback.message.answer(
         text="🎵 Выберите тариф Spotify:", reply_markup=build_subscription_kb()
    )

    await state.set_state(Request.subscription_plan)


@router.callback_query(YesNoCallbackData.filter(F.action == YesNoAction.no))
async def handle_no(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    await state.update_data(account_type="new")

    await callback.message.delete()

    await callback.message.answer(
         text="🎵 Выберите тариф Spotify:", reply_markup=build_subscription_kb()
    )
    await state.set_state(Request.subscription_plan)    


@router.callback_query(SubscriptionCallbackData.filter(F.plan == SubscriptionPlan.back))
async def handle_subscription_back(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await state.clear()
    await callback.message.delete()
    await callback.message.answer(
        text="У вас уже есть подписка на Spotify?",
        reply_markup=build_yes_no_inline_kb(),
    )


@router.callback_query(SubsPeriodCallbackData.filter(F.period == SubscriptionPeriod.back))
async def handle_period_back(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await state.set_state(Request.subscription_plan)
    await callback.message.delete()
    await callback.message.answer(
        text="🎵 Выберите тариф Spotify:", reply_markup=build_subscription_kb(),
    )


@router.callback_query(SubscriptionCallbackData.filter())
async def handle_sub_plan(
    callback: types.CallbackQuery,
    callback_data: SubscriptionCallbackData,
    state: FSMContext,
):
    plan = callback_data.plan
    await state.update_data(plan=plan.value)

    await state.set_state(Request.period)

    await callback.message.delete()

    await callback.message.answer(
        "👇 Выберите срок подписки:", reply_markup=build_plan_period_kb(),
    )


@router.callback_query(SubsPeriodCallbackData.filter())
async def handle_plan_period(
    callback: types.CallbackQuery,
    callback_data: SubsPeriodCallbackData,
    state: FSMContext,
):
    period = callback_data.period
    await state.update_data(period=period.value)

    data = await state.get_data()

    await callback.message.delete()

    if data.get("account_type") == "new":
        await state.set_state(Request.email_only)
        await callback.message.answer(text=ServiceForms.EMAIL_ONLY_TEXT)
    else:
        await state.set_state(Request.email)
        await callback.message.answer(text=ServiceForms.EMAIL_PROMPT)


@router.message(Request.email_only)
async def handle_email_only(
    message: types.Message,
    state: FSMContext,
):
    try:
        emailinfo = validate_email(message.text, check_deliverability=False)
        normalized_email = emailinfo.normalized.lower()
    except EmailNotValidError:
        await message.answer(ServiceForms.INCORRECT_EMAIL)
        return
    
    await message.delete()

    await state.update_data(email=normalized_email)
    username = message.from_user.username

    

    data = await state.get_data()
    await message.answer(
        text=ServiceForms.get_email_only_request_text(data=data, username=username),
        reply_markup=build_email_only_inline_kb(),
    )
    

@router.callback_query(EmailOnlyCallbackData.filter(F.action == EmailOnlyAction.submit))
async def handle_email_only_submit(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    data = await state.get_data()
    username = callback.from_user.username
    
    await callback.bot.send_message(
        chat_id=settings.admin_chat_id,
        text=ServiceForms.get_email_only_request_text(data=data, username=username)
    )
    await callback.message.delete()
    await state.clear()
    await callback.message.answer(text=ServiceForms.SUCCESS_SUBMIT_TEXT)


@router.callback_query(EmailOnlyCallbackData.filter(F.action == EmailOnlyAction.edit_email))
async def handle_edit_email_only(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await state.set_state(Request.email_only)
    await callback.message.answer(text=ServiceForms.EMAIL_PROMPT)


@router.message(Request.email)
async def handle_email(
    message: types.Message,
    state: FSMContext,
):
    try:
        emailinfo = validate_email(message.text, check_deliverability=False)
        normalized_email = emailinfo.normalized.lower()
    except EmailNotValidError as e:
        await message.answer(ServiceForms.INCORRECT_EMAIL)
        return
    
    await state.update_data(email=normalized_email)
    await message.delete()
    data = await state.get_data()

    if data.get("password"):
        username = message.from_user.username
        await message.answer(
            text=ServiceForms.get_request_text(
                data=data, username=username,
            ),
            reply_markup=build_confirm_inline_kb(),
        )
    else:  
        await state.set_state(Request.password)
        await message.answer(text=ServiceForms.PASSWORD_PROMPT)


@router.message(Request.password)
async def handle_password(
    message: types.Message,
    state: FSMContext,
):
    password = message.text

    if len(password) < 8:
        await message.answer("❌ Пароль должен содержать минимум 8 символов")
        return
        
    if not password.isascii():
        await message.answer("❌ Пароль должен содержать только латинские буквы и символы")
        return
        
    current_data = await state.get_data()

    await state.update_data(password=message.text)
    updated_data = await state.get_data()

    username = message.from_user.username

    await message.delete()
    await message.bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id - 1,
    )

    await message.answer(
        text=ServiceForms.get_request_text(
            data=updated_data, username=username
        ),
        reply_markup=build_confirm_inline_kb(),
    )


@router.callback_query(ReviewActionCallbackData.filter(F.action == ReviewAction.submit))
async def handle_submit(
    callback: types.CallbackQuery,
    state: FSMContext,
):
    data = await state.get_data()
    username = callback.from_user.username

    await callback.bot.send_message(
        chat_id=settings.admin_chat_id,
        text=ServiceForms.get_request_text(
            data=data, username=username,
    ),
    )
    await state.clear()
    await callback.message.delete()
    await callback.message.answer(text=ServiceForms.SUCCESS_SUBMIT_TEXT)


@router.callback_query(ReviewActionCallbackData.filter(F.action == ReviewAction.edit))
async def handle_edit(
    callback: types.CallbackQuery,
    state: FSMContext | None = None,
):
    await callback.message.delete()
    await callback.message.answer(
        text=ServiceForms.EDIT_CHOICE_TEXT,
        reply_markup=build_edit_data_inline_kb(),
    )


@router.callback_query(EditActionCallbackData.filter(F.action == EditAction.email))
async def handle_edit_email(
    callback: types.CallbackQuery,
    state: FSMContext
):
    await state.set_state(Request.email)
    await callback.message.answer(text=ServiceForms.EMAIL_PROMPT)


@router.callback_query(EditActionCallbackData.filter(F.action == EditAction.password))
async def handle_edit_password(
    callback: types.CallbackQuery,
    state: FSMContext
):
    previous_data = await state.get_data()
    await state.set_data(previous_data)

    await state.set_state(Request.password)
    await callback.message.answer(text=ServiceForms.PASSWORD_PROMPT)