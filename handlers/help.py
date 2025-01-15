from telebot import types
from loader import bot
from structure_example.history.history_data import log_user_request

@bot.message_handler(commands=['help'])
def help_info(message: types.Message)-> None:
    """
        Обрабатывает команду /help и отправляет информацию о доступных командах.

        :param message: Сообщение от пользователя, содержащие команду /help.
        """
    log_user_request('/help', message.from_user.id)
    bot.send_message(message.chat.id, 'Чтобы вам помочь выберите команду /train либо команду /plane ')
