from structure_example.utils import set_default_commands
from handlers.start import bot




if __name__ == '__main__':
    set_default_commands(bot)
    bot.polling(none_stop=True)