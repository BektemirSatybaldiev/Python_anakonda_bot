from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)

button_toyota_ist: KeyboardButton = KeyboardButton('тойота_ист')
button_honda_fit: KeyboardButton = KeyboardButton('хонда_фит')
button_toyota_raum: KeyboardButton = KeyboardButton('тойота_раум')
button_toyota_prius: KeyboardButton = KeyboardButton('тойота_приус')

keyboard.add(button_toyota_ist, button_honda_fit, button_toyota_raum, button_toyota_prius)
