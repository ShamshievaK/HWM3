# from config import bot, dp
# from aiogram import types, Dispatcher
# from db import db_main
#
#
#
#
# # async def start(message: types.Message):
# #     await bot.send_message(chat_id=message.from_user.id, text=f'Hello {message.from_user.first_name}')
# #     await db_main.sql_create()
#
#
# def register_start(dp: Dispatcher):
#     dp.register_message_handler(start, commands="start")