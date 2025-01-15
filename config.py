from dotenv import load_dotenv
import os
from typing import Tuple

# Загружаем переменные окружения из .env файла
load_dotenv()

# API ключ для доступа к API
API_KEY: str = os.getenv("RAPID_API_KEY")

# Токен бота для работы с Telegram API
BOT_TOKEN: str = os.getenv("BOT_TOKEN")

# Команды по умолчанию для бота
DEFAULT_COMMANDS: Tuple[Tuple[str, str], ...] = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ('train', 'Расписание поездов'),
    ('plane', 'Расписание самолетов'),
    ('history', 'История запросов'))
