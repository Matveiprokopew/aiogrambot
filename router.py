from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

rt = Router()

@rt.message(Command("t"))
async def start(message: Message):
	await message.answer('Привет!')