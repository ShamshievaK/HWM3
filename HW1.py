# import logging
# from aiogram import types
from aiogram import executor
from buttons import start
from config import bot, dp, admin
from handlers import start, commands, echo, quiz



start.register_start(dp)
commands.register_commands(dp)
quiz.register_quiz(dp)

echo.register_echo(dp)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)