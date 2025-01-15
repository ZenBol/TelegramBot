from telebot import TeleBot
from telebot.types import BotCommand
from config import DEFAULT_COMMANDS


def set_default_commands(bot: TeleBot) -> None:
    """
        Устанавливает команды по умолчанию для бота.

        :param bot: Экземпляр бота, для которого устанавливаются команды.
        """
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
