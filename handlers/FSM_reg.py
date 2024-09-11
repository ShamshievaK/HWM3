from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class FSM_store(StatesGroup):
    tovar = State()
    razmer = State()
    category = State()
    price = State()
    photo = State()

async def start_fsm_store(message: types.Message):
    await message.answer('Введите название товара: ')
    await FSM_store.tovar.set()

async def load_tovar(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("XL"), KeyboardButton("3XL"), KeyboardButton("L"), KeyboardButton("M"),
               KeyboardButton("S"))
    async with state.proxy() as data:
        data['tovar'] = message.text

    await message.answer('Размер: ', reply_markup=markup)
    await FSM_store.next()

async def load_razmer(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['razmer'] = message.text

    await message.answer('Категория товара: ')
    await FSM_store.next()

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('Цена: ')
    await FSM_store.next()

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('Отправьте фото: ')
    await FSM_store.next()

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data['photo'],
                               caption=f'Верны ли данные?\n\n'
                               f'Название товара: {data["tovar"]}\n\n'
                               f'Размер товара: {data["razmer"]}\n\n'
                               f'Категория товара: {data["category"]}\n\n'
                               f'Цена товара: {data["price"]}\n\n')
    await state.finish()

def register_fsm_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['store'])
    dp.register_message_handler(load_tovar, state=FSM_store.tovar)
    dp.register_message_handler(load_razmer, state=FSM_store.razmer)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])


