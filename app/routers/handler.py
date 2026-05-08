from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from app.keyboards import role_keyboard

from app.databases.requests import get_role, async_set_user

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    roles = await get_role()
    await message.answer('Wellcome to our team. Yo`ve to choose your role before starting find job.', reply_markup=role_keyboard(roles))


@router.callback_query(F.data.startswith('role_'))
async def set_user(callback: CallbackQuery):
    role_id = callback.data.split('_')[1]

    id = callback.from_user.id

    try:
        await async_set_user(id, role_id)
        await callback.message.answer('Success')
    except Exception as e:
        await callback.message.answer('Error in adding to db')
        print('====')
        print(e)
        print('====')
    