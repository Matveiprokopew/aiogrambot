from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

rt = Router()

@rt.message(Command("t"))
async def start(message: Message):
	await message.answer('Привет!')

@rt.message(Command("start"))
async def start(message: Message):
    
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_name = message.from_user.full_name

    welcome_text = f"""Привет, {user_first_name}!"""
    photo = FSInputFile("assets/welcome_photo.jpg")

    await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=welcome_text)
    await message.answer("Скоро тут будет меню")
