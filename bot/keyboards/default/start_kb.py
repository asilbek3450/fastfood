from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[  # menu, biz haqimizda, kontakt
    [KeyboardButton('🍽️ MENU'), KeyboardButton('📖 Biz haqimizda')],
    [KeyboardButton('📞 Kontakt')], [KeyboardButton('✍️ Adminga xabar yuborish')]
])

start_admin_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('🍽️ MENU')],
    [KeyboardButton('🔖 Kategoriyalar ro\'yhati'), KeyboardButton('🍔 Taomlar ro\'yhati')],
    [KeyboardButton('➕ Kategoriya qo`shish'), KeyboardButton('➕ Taom qo`shish')],
    [KeyboardButton('❌ Taomni o`chirish')],
    [KeyboardButton('📞 Dasturchi bilan aloqa')]
])

