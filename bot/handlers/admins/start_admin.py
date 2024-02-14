from aiogram import types

from bot.config import ADMINS
from bot.keyboards.default.start_kb import start_admin_keyboards
from bot.loader import dp


# start_admin_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
#     [KeyboardButton('🍽️ MENU')],
#     [KeyboardButton('🔖 Kategoriyalar ro\'yhati'), KeyboardButton('🍔 Taomlar ro\'yhati')],
#     [KeyboardButton('➕ Kategoriya qo`shish'), KeyboardButton('➕ Taom qo`shish')],
#     [KeyboardButton('❌ Taomni o`chirish')],
#     [KeyboardButton('📞 Dasturchi bilan aloqa')]
# ])
#

@dp.message_handler(user_id=ADMINS, commands='start')
async def admin_start(message: types.Message):
    await message.answer('Admin panel', reply_markup=start_admin_keyboards)

