from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_hi = KeyboardButton('/мотивация')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)