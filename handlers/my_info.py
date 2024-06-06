from aiogram import Router, types
from aiogram.filters.command import Command


info_router=Router()


@info_router.message(Command ("my_info"))
async def my_info_handler(message: types.Message):
    await message.answer(f'Информация о вас \n Имя: {message.from_user.first_name} \n Ваш ник:{message.from_user.username} \n Ваш id: {message.from_user.id} ')


