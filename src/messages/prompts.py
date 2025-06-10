class ServiceForms:
    EMAIL_PROMPT =( 
        "✉️ <b>Введите ваш email</b>\n"
        "Например: <i>example@gmail.com</i>"
    )

    INCORRECT_EMAIL = (
        "❌ Неверный email\n"
        "Пример: example@gmail.com\n"
        "Попробуйте ещё раз:"
    )

    PASSWORD_PROMPT = (
        "🌟 <b>Последний шаг!</b>\n"
        "Введите пароль от вашего Spotify\n\n"
        "Мы гарантируем конфиденциальность"
    )

    @staticmethod
    def get_request_text(data: dict, username: str) -> str:
        return (
            "✅ <b>Заявка успешно оформлена!</b>\n\n"
            "┏━━━━━━━━━━━━━━━━━━━┓\n"
            f"<b>🔹 Сервис:</b>  {data.get('service', '❌').capitalize()}\n"
            f"<b>🔹 Тариф:</b>    {data.get('plan', '❌')}\n"
            f"<b>🔹 Срок:</b>      {data.get('period', '❌')}\n"
            f"<b>🔹 Email:</b>     <code>{data.get('email', '❌')}</code>\n"
            f"<b>🔹 Пароль:</b>     <code>{data.get('password')}</code>\n"
            f"<b>🔹 Username:</b>   @{username}\n"
            "┗━━━━━━━━━━━━━━━━━━━┛\n\n"
            "⌛ Обычно активация занимает <b>5-15 минут</b>\n"
            "📩 Вы получите уведомление по окончании\n\n"
            "<i>Спасибо за выбор нашего сервиса!</i>"
        )

    SUCCESS_SUBMIT_TEXT = (
    "<b>✅ Ваша заявка принята!</b>\n\n"
    "Оператор получил ваши данные и свяжется в ближайшее время.\n"
    "<i>⌛ Среднее время ответа: 15 минут</i>\n"
    "<i>📞 Если у вас есть вопросы или нужна помощь — напишите нам в личные сообщения, @podpiski_tm</i>\n\n"
    "Спасибо за доверие! 💙"
    )

    EDIT_CHOICE_TEXT = (
    "✏️ <b>Что хотите изменить?</b>\n"
    "Выберите поле для редактирования:"
    )

