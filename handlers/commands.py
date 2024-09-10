from aiogram import types, Dispatcher
import os
from buttons import start
from config import bot, dp


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello!', reply_markup=start)

async def mem_handler(message: types.Message):
    folder = 'media'
    photo_path = os.path.join(folder, 'img.png')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo)

async def mem_all_handler(message: types.Message):
    folder = 'media'
    photos = os.listdir(folder)
    for photo_name in photos:
        photo_path = os.path.join(folder, photo_name)
        if photo_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            with open(photo_path, 'rb') as photo:
                await bot.send_photo(chat_id=message.from_user.id, photo=photo)

async def music_handler(message: types.Message):
    folder = 'audio'
    music_name = "track.mp3"
    music_path = os.path.join(folder, music_name)
    with open(music_path, 'rb') as music:
        await message.answer_audio(music)

async def file_handler(message: types.Message):
    await bot.send_document(chat_id=message.from_user.id,document=open('main.py', 'rb'))

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands="start")
    dp.register_message_handler(mem_handler, commands="mem")
    dp.register_message_handler(mem_all_handler, commands="mem_all")
    dp.register_message_handler(music_handler, commands="music")
    dp.register_message_handler(file_handler, commands="file")