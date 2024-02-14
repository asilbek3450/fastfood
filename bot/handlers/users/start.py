from aiogram import types

from bot.keyboards.default.start_kb import start_admin_keyboards
from bot.loader import dp


# start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[  # menu, biz haqimizda, kontakt
#     [KeyboardButton('🍽️ MENU'), KeyboardButton('📖 Biz haqimizda')],
#     [KeyboardButton('📞 Kontakt')], [KeyboardButton('✍️ Adminga xabar yuborish')]
# ])


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Fast food restoraniga xush kelibsiz hurmatli {message.from_user.full_name}!\n', reply_markup=start_admin_keyboards)
