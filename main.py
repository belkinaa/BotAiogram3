from aiogram import Bot, Dispatcher, F
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import Command

from keyboards import Name_Buttons
from utils.commands import set_commands


from handlers.start import get_start
from state.register import RegisterState
from handlers.register import start_register, register_name, register_phone
load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(admin_id, text='Я запустил бота')

dp.startup.register(start_bot)

# 2 аргумент [Command()] - фильтр, при котором будет вызван этот handler
dp.message.register(get_start, Command(commands='start'))

# регистрируем хендлеры
dp.message.register(start_register, F.text == Name_Buttons().register)
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone, RegisterState.regPhone)

async def start():
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())