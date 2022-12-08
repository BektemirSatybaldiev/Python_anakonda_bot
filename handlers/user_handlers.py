from aiogram import types
from keyboards.keyboard_utils import keyboard, button_toyota_ist, button_honda_fit, button_toyota_raum, \
    button_toyota_prius
from services import cars_prices


async def process_start_command(message: types.Message):
    await message.answer('Средняя цена авто в Бишкеке', reply_markup=keyboard)


async def process_toyota_ist_answer(message: types.Message):
    await message.answer(cars_prices.get_model_price(button_toyota_ist.text))


async def process_honda_fit_answer(message: types.Message):
    await message.answer(cars_prices.get_model_price(button_honda_fit.text))


async def process_toyota_raum_answer(message: types.Message):
    await message.answer(cars_prices.get_model_price(button_toyota_raum.text))


async def process_toyota_prius_answer(message: types.Message):
    await message.answer(cars_prices.get_model_price(button_toyota_prius.text))
