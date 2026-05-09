from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from app.keyboards import role_keyboard, find_job_kb, employer_kb
from app.databases.requests import (
    get_role,
    async_set_user,
    get_user_by_id,
    change_role
)

router = Router()


# ---------------- START ----------------
@router.message(CommandStart())
async def cmd_start(message: Message):
    user = await get_user_by_id(message.from_user.id)

    # NEW USER
    if not user:
        roles = await get_role()
        kb = role_keyboard(roles)

        await message.answer(
            "👋 Welcome to our platform!\n"
            "Please choose your role before getting started.",
            reply_markup=kb
        )
        return

    # EXISTING USER
    kb, text = get_dashboard_by_role(user.role_id)

    await message.answer(text, reply_markup=kb)


# ---------------- SET ROLE ----------------
@router.callback_query(F.data.startswith("role_"))
async def set_user_role(callback: CallbackQuery):
    role_id = int(callback.data.split("_")[1])

    success = await change_role(callback.from_user.id, role_id)

    if success:
        kb, text = get_dashboard_by_role(role_id)

        await callback.message.answer(
            "✅ Role successfully selected!\n\n" + text,
            reply_markup=kb
        )
    else:
        await callback.message.answer("❌ Error while saving role")


# ---------------- CHANGE ROLE ----------------
@router.callback_query(F.data.startswith("change_role"))
async def change_role_handler(callback: CallbackQuery):
    user = await get_user_by_id(callback.from_user.id)

    new_role = 2 if user.role_id == 3 else 3

    success = await change_role(callback.from_user.id, new_role)

    if success:
        kb, text = get_dashboard_by_role(new_role)
        
        await callback.message.delete()
        await callback.message.answer(
            "✅ Role successfully updated!\n\n" + text,
            reply_markup=kb
        )
# ---------------- ROLE DASHBOARD ----------------
def get_dashboard_by_role(role_id: int):
    if role_id == 2:
        return find_job_kb, "🔎 Job Seeker dashboard"
    elif role_id == 3:
        return employer_kb, "🏢 Employer dashboard"
    else:
        return find_job_kb, "Choose your role"