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

find_job_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Find job', callback_data='find_category'),InlineKeyboardButton(text='News', callback_data='news'), InlineKeyboardButton(text='Callback', callback_data='callback')],
    [InlineKeyboardButton(text='Change Role', callback_data='change_role_2')]
])

employer_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Create Vacancy', callback_data='create_vacancy'), InlineKeyboardButton(text='My Job Posts', callback_data='my_job_posts'), InlineKeyboardButton(text='Vacancy Statistics', callback_data='vacancy_statistics')],
    [InlineKeyboardButton(text='Change Role', callback_data='change_role_3')]
])