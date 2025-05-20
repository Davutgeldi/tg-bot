from aiogram import Router, types
from aiogram.filters import CommandStart, Command


router = Router(name="base_commands_router")


@router.message(CommandStart())
async def handle_start(message: types.Message):
    welcome_text = """
        🌟 <b>Добро пожаловать в бота для оплаты онлайн-сервисов!</b> 🌟

        Я помогу вам быстро и безопасно оплатить подписки на популярные сервисы:

        • Apple Music
        • Spotify 
        • YouTube Premium
        • И многие другие

        <b>Как это работает?</b>
        1. Создаете заявку командой /new_request
        2. Выбираете сервис и сумму
        3. Получаете реквизиты для оплаты
        4. После оплаты получаете доступ к сервису

        ⚡ <i>Мгновенная активация после оплаты</i>
        🔒 <i>Безопасные платежи</i>
        🔄 <i>Автопродление подписок</i>

        Начните с команды /new_request или посмотрите /help для справки
            """
    await message.answer(welcome_text)


@router.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer("This is help message")
