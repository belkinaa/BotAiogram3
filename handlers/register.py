from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re
import os
from utils.database import Database

async  def start_register(message: Message, state: FSMContext):
    db = Database(os.getenv('DATABASE_NAME'))
    user = db.select_user_id(message.from_user.id)
    if user:
        await message.answer(f'{user[1]}, Вы уже зарегистированы')
    else:
        await message.answer('Как тебя зовут?')
        # устанавливаем состояние ожидание ввода имени пользователя
        await state.set_state(RegisterState.regName)

# ф-ция срабатывает после ввода пользователем своего имени
async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Приятно познакомиться {message.text}\n'
                         f'Укажи номер телефона')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhone)

async def register_phone(message:Message, state:FSMContext):
    if (re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)

        reg_data = await state.get_data()

        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')

        msg = f'Твои данные: {reg_name} / {reg_phone}'
        await message.answer(msg)
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, message.from_user.id)
        await state.clear()
    else:
        await message.answer('Неверно указан формат телефона')