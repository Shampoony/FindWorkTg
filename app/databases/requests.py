from app.databases.models import User, Role, async_session
from sqlalchemy import select, delete, update

async def get_role():
    async with async_session() as session:
        roles = await session.execute(select(Role))
        return roles.scalars().all()
    
async def async_set_user(tg_id: int, role_id: int):
    async with async_session() as session:
        user = User(
            tg_id=tg_id,
            role_id=role_id
        )

        session.add(user)
        await session.commit()