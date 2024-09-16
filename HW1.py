import logging
from aiogram import types
from aiogram.utils import executor
from buttons import start
from config import bot, dp, admin
from handlers import start, commands, echo, quiz, FSM_reg
from db import db_main



start.register_start(dp)
commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_reg.register_store(dp)


echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)