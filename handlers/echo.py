import asyncio

from aiogram import types, Dispatcher, Bot

from config import bot, dp, TOKEN
import random



games=['🎲', '⚽️', '🏀', '🎯', '🎳']


async def echo(message: types.Message):
    text = message.text

    try:
        if text.isdigit():
            await message.answer(int(text)**2)
        elif text == 'game':
            random_game= random.choice(games)
            # await bot.send_dice(
            #     chat_id=message.from_user.id,
            #     emoji=random_game,
            # )
            bot_dice = await bot.send_dice(chat_id=message.from_user.id, emoji=random_game)
            user_dice = await bot.send_dice(chat_id=message.from_user.id, emoji=random_game)
            bot_data = bot_dice["dice"]["value"]
            user_data = user_dice["dice"]["value"]
            if bot_data > user_data:
                bot.reply_to(message, "Бот победил")
            elif user_data > bot_data:
                bot.reply_to(message, "Ты победил")
            else:
                bot.reply_to(message, "Ничья")

        else:
            await message.answer(text)

    except ValueError:
        print('ошибка')






def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)