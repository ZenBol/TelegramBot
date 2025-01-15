import requests
from structure_example.my_dict.months_dict import format_datetime
from  typing import Optional, Dict


def api_search(from_station_code: str, to_station_code: str, travel_date: str, transport_types: str, api_key: str) -> Optional[Dict[str, str]]:
    """
        Выполняет поиск рейсов между станциями по заданным параметрам.

        :param from_station_code: Код станции отправления.
        :param to_station_code: Код станции назначения.
        :param travel_date: Дата путешествия в формате 'YYYY-MM-DD'.
        :param transport_types: Тип транспорта для поиска (например, 'plane', 'train').
        :param api_key: Ключ API для доступа к сервису.
        :return: Словарь с информацией о рейсе (время отправления, время прибытия, продолжительность) или None, если рейсы не найдены.
        """
    API_URL = (f'https://api.rasp.yandex.net/v3.0/search/?apikey={api_key}&format=json'
               f'&from={from_station_code}&to={to_station_code}&lang=ru_RU&transport_types={transport_types}&page=1&date={travel_date}')

    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data['pagination']['total'] > 0:
            first_trip = data['segments'][0]
            departure_time = format_datetime(first_trip['departure'])
            arrival_time = format_datetime(first_trip['arrival'])
            total_minutes = first_trip['duration'] // 60  # Общее время в минутах

            # Вычисляем дни, часы и минуты
            days = total_minutes // (24 * 60)  # Количество дней
            hours = (total_minutes % (24 * 60)) // 60  # Остаток часов
            minutes = total_minutes % 60  # Остаток минут
            duration_info = f"{int(days)} дней {int(hours)} часов {int(minutes)} минут."

            return {
                'departure_time': departure_time,
                'arrival_time': arrival_time,
                'duration_info': duration_info
            }

        print("Ошибка при запросе к API:", response.status_code)
        print("Текст ответа:", response.text)

        return None
