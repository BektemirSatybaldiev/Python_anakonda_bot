from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)

button_toyota_ist: KeyboardButton = KeyboardButton('toyota_ist')
button_honda_fit: KeyboardButton = KeyboardButton('honda_fit')
button_toyota_raum: KeyboardButton = KeyboardButton('toyota_raum')
button_toyota_prius: KeyboardButton = KeyboardButton('toyota_prius')

keyboard.add(button_toyota_ist, button_honda_fit, button_toyota_raum, button_toyota_prius)
