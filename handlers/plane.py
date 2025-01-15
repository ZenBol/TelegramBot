from telebot import types
from loader import bot
from structure_example.config import API_KEY
from structure_example.my_dict.stations_dict import stations_dict
from structure_example.my_dict.transport_dict import transport_dict
from structure_example.api_config import api_search
from structure_example.history.history_data import log_user_request


@bot.message_handler(commands=['plane'])
def start(message: types.Message) -> None:
    """
       Обрабатывает команду /plane и запрашивает у пользователя город вылета.

       :param message: Сообщение от пользователя, содержащие команду /plane.
       """
    log_user_request('/plane', message.from_user.id)
    bot.send_message(message.chat.id, "Добрый день! Введите город вылета:")
    bot.register_next_step_handler(message, get_from_city)

def get_from_city(message: types.Message) -> None:
    """
       Обрабатывает ввод города вылета от пользователя.

       :param message: Сообщение от пользователя, содержащее город вылета.
       """
    from_city = message.text
    bot.send_message(message.chat.id, "Введите город прилета:")
    bot.register_next_step_handler(message, get_to_city, from_city)

def get_to_city(message: types.Message, from_city: str) -> None:
    """
        Обрабатывает ввод города прилета от пользователя.

        :param message: Сообщение от пользователя, содержащее город прилета.
        :param from_city: Город вылета, введенный пользователем на предыдущем шаге.
        """
    to_city = message.text
    bot.send_message(message.chat.id, "Введите дату в формате Год-Месяц-День:")
    bot.register_next_step_handler(message, get_travel_date, from_city, to_city)

def get_travel_date(message: types.Message, from_city: str, to_city: str) -> None:
    """
        Обрабатывает ввод даты путешествия от пользователя и запрашивает информацию о рейсе.

        :param message: Сообщение от пользователя, содержащее дату путешествия.
        :param from_city: Город отправления.
        :param to_city: Город назначения.
        """
    travel_date = message.text

       # Получаем коды станций из словаря
    from_station_code = stations_dict.get(from_city)
    to_station_code = stations_dict.get(to_city)

    if not from_station_code or not to_station_code:
        bot.send_message(message.chat.id, "Одна из введенных станций не найдена. Пожалуйста, проверьте написание.")
        return

    transport_types = 'plane'
    transport_name = transport_dict["plane"]

    # Запрос с API через функцию api_search
    trip_data = api_search(from_station_code, to_station_code, travel_date, transport_types, API_KEY)

    if trip_data:
        departure_time = trip_data['departure_time']
        arrival_time = trip_data['arrival_time']
        duration_info = trip_data['duration_info']

        trip_info = (
            f"Расписание на {transport_name} из {from_city} в {to_city} на {travel_date}:\n"
            f"Время отправления: {departure_time}\n"
            f"Время прибытия: {arrival_time}\n"
            f"Продолжительность: {duration_info}."
        )
        bot.send_message(message.chat.id, trip_info)
    else:
        bot.send_message(message.chat.id, "К сожалению, рейсов не найдено.")
