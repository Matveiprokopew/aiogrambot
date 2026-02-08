import logging 
import asyncio # Импортируем обязательно "asyncio" для написания асинхронного кода
import os # Импортируем "os" для чтения переменного окружения
from dotenv import load_dotenv # За ним же из "dotenv", импортируем "load_dotenv"

load_dotenv() # Подгружаем из ".env"

from aiogram import Bot, Dispatcher # Необходимо для запуска и дальнейшей логики бота

from handlers.command_rt import rt
from handlers.callback_rt import callback_rt
from database.models import async_main

bot = Bot(token=os.getenv('TOKEN')) # Берем токен

dp = Dispatcher() # Корневой роутер (обработка входящих обновлений)

async def main():
    #   dp.include_routers(user, creator) для 2ух и > роутеров
    dp.include_routers(rt, callback_rt) # Подключаем роутер
    dp.startup.register(startup)
    await bot.delete_webhook(drop_pending_updates=True) # Тем самым, сообщения, которые были отправлены боту, когда он был выключен, при включении будут игнорироваться
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):  # !!!
    await async_main()


if __name__  == '__main__':
    logging.basicConfig(level=logging.INFO) # Подключаем logging
    print('Бот включен!')
    try:
        asyncio.run(main())  
    except KeyboardInterrupt:
        print('Бот выключен!')


"""
Фамилия: {last_name if last_name else 'Не указана'}
    ├ Username: @{username if username else 'Не указан'}
"""
