from aiogram import Bot
from aiogram.types import Message
from keyboards.profile_kb import profile_kb
from utils.database import Database
import os
from keyboards.register_kb import register_keyboard


async def get_start(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    user = db.select_user_id(message.from_user.id)
    if user:
        await bot.send_message(message.from_user.id, f'Hi {user[1]}', reply_markup=profile_kb)
    else:
        await bot.send_message(message.from_user.id, 'Сообщение из get_start', reply_markup=register_keyboard)