import logging

from aiogram import Dispatcher

from bot.config import ADMINS
from bot.keyboards.default.start_kb import start_admin_keyboards


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi", reply_markup=start_admin_keyboards)

        except Exception as err:
            logging.exception(err)
