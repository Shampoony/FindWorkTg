from app.databases.models import User, Role, async_session
from sqlalchemy import select, update


async def get_role():
    async with async_session() as session:
        result = await session.execute(select(Role))
        return result.scalars().all()


async def get_user_by_id(tg_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.tg_id == tg_id)
        )
        return result.scalars().first()


async def async_set_user(tg_id: int, role_id: int):
    async with async_session() as session:
        user = User(tg_id=tg_id, role_id=role_id)

        session.add(user)
        await session.commit()


async def change_role(tg_id: int, role_id: int):
    async with async_session() as session:
        stmt = (
            update(User)
            .where(User.tg_id == tg_id)
            .values(role_id=role_id)
        )

        result = await session.execute(stmt)
        await session.commit()

        return result.rowcount > 0