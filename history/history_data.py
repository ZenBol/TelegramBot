from peewee import *
from datetime import datetime
from typing import List

db = SqliteDatabase('user_request.db')
class UserRequest(Model):
    """
        Модель для хранения запросов пользователей.

        Attributes:
            user_id (int): Идентификатор пользователя.
            command (str): Команда, введенная пользователем.
            time (datetime): Время запроса.
        """
    user_id: int = IntegerField()
    command: str = TextField()
    time: datetime = DateTimeField()

    class Meta:
        database = db  # Используем базу данных SQLite

# Создание таблицы, если она не существует
db.connect()
db.create_tables([UserRequest], safe=True)

def log_user_request(command: str, user_id: int) -> None:
    """
        Логирует запрос пользователя в базе данных.

        :param command: Команда, которую ввел пользователь.
        :param user_id: Идентификатор пользователя.
        """
    request_time = datetime.now()
    UserRequest.create(user_id=user_id, command=command, time=request_time)


def get_request_history() -> str:
    """
       Получает историю запросов пользователей из базы данных.

       :return: Строка с историей запросов.
       """
    history = UserRequest.select()
    result: List[str] = []
    for request in history:
        # Форматируем время
        formatted_time = request.time.strftime('%d.%m.%Y %H:%M:%S')
        result.append(f"User ID: {request.user_id}, Command: {request.command}, Time: {formatted_time}")
    return "\n".join(result)