from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import ENGINE

engine = create_async_engine(ENGINE, echo=True)
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger)

    
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id'))
    role: Mapped['Role'] = relationship('Role', back_populates='users')
    


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()

    users: Mapped[list['User']] = relationship('User', back_populates='role')

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)