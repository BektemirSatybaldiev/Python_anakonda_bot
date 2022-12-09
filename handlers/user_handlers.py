from aiogram import types
from keyboards.keyboard_utils import keyboard
from lexicon.lexicon_en import main_menu
from lexicon.lexicon_ru import cars_ru
from services import cars_prices


async def process_main_menu(message: types.Message):
    await message.answer(main_menu[message.text])


async def process_start_command(message: types.Message):
    await message.answer('Хочешь узнать среднюю рыночную стоимость авто?\nВыбери свою марку автомобиля!',
                         reply_markup=keyboard)


async def process_car_answer(message: types.Message):
    await message.answer(cars_prices.get_model_price(cars_ru[message.text]))
