class OtherForms:
    @staticmethod
    def get_request_text(service: str, username: str) -> str:
        return (
            "✅ <b>Новая заявка</b>\n\n"
            "┏━━━━━━━━━━━━━━━━━━━┓\n"
            f"<b>🔹 Сервис:</b>  {service.capitalize()}\n"
            f"<b>🔹 Username:</b>   @{username}\n"
            "┗━━━━━━━━━━━━━━━━━━━┛\n\n"
        )
    
    SUCCESS_SUBMIT_TEXT = (
    "<b>✅ Ваша заявка принята!</b>\n\n"
    "Оператор получил ваши данные и свяжется в ближайшее время.\n"
    "<i>⌛ Среднее время ответа: 15 минут</i>\n\n"
    "<i>📞 Если у вас есть вопросы или нужна помощь — напишите нам в личные сообщения, @podpiski_tm</i>\n\n"
    "Спасибо за доверие! 💙"
    )    


    OTHER_SERVICES_TEXT = """
✨ <b>Другие услуги</b>


🎮 <i>Игры:</i> Steam, PUBG, Fortnite, PS Store
💰 <i>Крипта:</i> Binance, Bybit  
🤖 <i>AI:</i> ChatGPT, Midjourney  
💳 <i>Платежи:</i> PayPal, WebMoney  
💵 <i>"Купить USDT"</i> 


Оператор ответит за 5 минут ⏳
"""