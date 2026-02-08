from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # Новые импорты

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Расчистить снег", callback_data="snow", url="")],
        [InlineKeyboardButton(text="support", callback_data='support', url="")],
    ]
)
