from aiogram.fsm.state import State, StatesGroup


class Request(StatesGroup):
    service = State()
    subscription_plan = State()
    period = State()
    email = State()
    email_only = State()
    password = State()