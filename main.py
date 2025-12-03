import logging 
import asyncio # Импортируем обязательно "asyncio" для написания асинхронного кода
import os # Импортируем "os" для чтения переменного окружения
from dotenv import load_dotenv # За ним же из "dotenv", импортируем "load_dotenv"

load_dotenv() # Подгружаем из ".env"

from aiogram import Bot, Dispatcher # Необходимо для запуска и дальнейшей логики бота
from aiogram.types import Message # Для обработки типа сообщений
from aiogram.filters import CommandStart # Импортируем, чтобы обработать команду /start

bot = Bot(token=os.getenv('TOKEN')) # Берем токен

dp = Dispatcher() # Корневой роутер (обработка входящих обновлений)


@dp.message(CommandStart()) # Роутер, который обрабатывает сообщение /start
async def start(message: Message): # Принимает объект "message" типа "Message"
    await message.reply('Привет!') # Подразумевает ответ бота на /start обычным сообщением, а не ответом на сообщение
    await message.answer("Скоро тут будет меню")


async def main():
    await bot.delete_webhook(drop_pending_updates=True) # Тем самым, сообщения, которые были отправлены боту, когда он был выключен, при включении будут игнорироваться
    await dp.start_polling(bot)
  
if __name__  == '__main__':
    logging.basicConfig(level=logging.INFO) # Подключаем logging
    print('Бот включен!')
    try:
        asyncio.run(main())  
    except KeyboardInterrupt:
        print('Бот выключен!')