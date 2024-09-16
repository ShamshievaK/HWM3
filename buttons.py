from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)
start_buttons = KeyboardButton('/start')
mem_buttons = KeyboardButton('/mem')
mem_all_buttons = KeyboardButton('/mem_all')
music_buttons = KeyboardButton('/music')
file_buttons = KeyboardButton('/file')
quiz_buttons = KeyboardButton('/quiz')






start.add(start_buttons, mem_buttons, mem_all_buttons, music_buttons, file_buttons, quiz_buttons)


cancel_button = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))
submit_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                    row_width=2).add(KeyboardButton('Да'), KeyboardButton('Нет'))
