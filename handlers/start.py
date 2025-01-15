from telebot import types
from loader import bot
from structure_example.history.history_data import log_user_request
@bot.message_handler(commands=['start'])
def welcome(message: types.Message) -> None:
    """
        Приветствует пользователя и предоставляет информацию о доступных командах.

        :param message: Сообщение от пользователя, содержащие команду /start.
        """
    log_user_request('/start', message.from_user.id)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}{message.from_user.last_name} '
                                      f'я бот который помогает искать расписание поездов и самолетов на определенную дату.'
                                      f'Для того чтобы найти расписание поезда введите /train '
                                      f'расписание самолетов /plane '
                                      f'для вывода справки введите /help')