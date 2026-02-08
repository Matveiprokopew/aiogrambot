from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InputMediaPhoto

from database.requests import set_user, set_status
from keyboards.user_kb import main 


rt = Router()

@rt.message(Command("t"))
async def start(message: Message):
	await message.answer('Привет!')

@rt.message(Command("start"))
async def start(message: Message):

    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_name = message.from_user.full_name

    photo = FSInputFile("assets/photo.png")
    photo1 = FSInputFile("assets/photo1.jpg") 
    welcome_text = f"""Привет, {user_first_name}!"""
    media = [
            InputMediaPhoto(media=photo, caption=welcome_text),  # первое фото с подписью
            InputMediaPhoto(media=photo1)  # второе фото без подписи
]
    await set_user(message.from_user.id)
    await set_status(message.from_user.id, "PLAYER")
    await message.bot.send_media_group(chat_id=message.chat.id, media=media)
    await message.answer("Скоро тут будет меню", reply_markup=main)



@rt.message(Command("test"))
async def start(message: Message):
    await set_status(message.from_user.id, "ADMIN")
    await message.answer("Привет, ADMIN!")
