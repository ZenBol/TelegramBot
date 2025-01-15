from datetime import datetime

# Словарь для месяцев на русском языке
months_dict: dict[int, str] = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}


def format_datetime(iso_string: str) -> str:
    """
       Форматирует строку даты в формате ISO в удобочитаемый вид.

       :param iso_string: Дата в формате ISO (например, '2023-01-14T15:30:00Z').
       :return: Строка с отформатированной датой (например, '14 января 2023, 15:30').
       """
    dt = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))

    # Форматируем дату вручную
    day = dt.day
    month = months_dict[dt.month]
    year = dt.year
    hour = dt.hour
    minute = dt.minute

    return f"{day} {month} {year}, {hour}:{minute:02d}"