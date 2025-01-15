from telebot import types
from loader import bot
from structure_example.history.history_data import get_request_history
from structure_example.history.history_data import log_user_request

@bot.message_handler(commands=['history'])
def handle_history(message: types.Message) -> None:
    """
        Обрабатывает команду /history и отправляет историю запросов пользователя.

        :param message: Сообщение от пользователя, содержащие команду /history.
        """
    log_user_request('/history', message.from_user.id)
    history = get_request_history()
    bot.reply_to(message, history if history else "История пуста.")
