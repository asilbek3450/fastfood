from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

contact = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📞 Telefon raqam yuborish', request_contact=True)]
])
