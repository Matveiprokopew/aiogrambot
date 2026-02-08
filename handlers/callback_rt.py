from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

callback_rt = Router()

@callback_rt.callback_query(F.data == "snow")
async def menu(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer("Меню для заказа недоступно")
