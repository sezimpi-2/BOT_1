from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
import random
import os

photo_router=Router()


@photo_router.message(Command("photo"))
async def picture_handler(message: types.Message):
    random_photo = random.choice(os.listdir('images'))
    photo = FSInputFile(f'images/{random_photo}')
    await message.reply_photo(photo, caption = 'Рандомная фото блюда из меню')