import asyncio
import logging
import sys


from aiogram import Dispatcher
from app.routers.handler import router

from config import bot

from app.databases.models import async_main

async def main():

    await async_main()

    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')