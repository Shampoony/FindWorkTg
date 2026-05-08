from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




def role_keyboard(roles):
    keyboard = InlineKeyboardBuilder()
    for el in roles:
        keyboard.add(InlineKeyboardButton(
            text=f'{el.title}',
            callback_data=f'role_{el.id}'
        ))
    return keyboard.adjust(len(roles)).as_markup()