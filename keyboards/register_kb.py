from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards import Name_Buttons

register_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text=Name_Buttons().register
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Для продолжения нажмите на кнопку'

)