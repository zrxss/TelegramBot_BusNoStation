import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession

import time

from config import BOT_TOKEN,TG_PROXY

from way_time import should_go_out



session = AiohttpSession(proxy=TG_PROXY)

BusBot = Bot(token=BOT_TOKEN, session=session)

dp = Dispatcher()



active_tasks = {}

@dp.message(CommandStart())
async def start_monitoring(message: Message):
    user_id = message.from_user.id
    if user_id not in active_tasks:
        await message.answer('Мониторинг прибытия включен')
        active_tasks[user_id] = asyncio.create_task(monitoring(message, user_id))
    else:
        await message.answer('Мониторинг уже запущен')
        return




async def monitoring(message: Message, user_id):
    timer = time.monotonic()
    while time.monotonic() - timer < 600:
        try:
            if await should_go_out():
                await message.answer('Выходи из дома!')
            await asyncio.sleep(5)
        finally:
            active_tasks.pop(user_id)
    else:
        await message.answer('Мониторинг прибытия окончен')
        active_tasks.pop(user_id)
        return



@dp.message(F.text == '/stop')
async def stop_monitoring(message: Message):
    user_id = message.from_user.id
    task = active_tasks.pop(user_id, False)
    if not task:
        await message.answer('Мониторинг не был запущен')
        return
    task.cancel()
    await message.answer('Мониторинг прекращен')


async def main():
    await dp.start_polling(BusBot)

if __name__ == '__main__':
    asyncio.run(main())