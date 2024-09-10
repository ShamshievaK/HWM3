from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

admin = [7327755300, ]