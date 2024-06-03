import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from aiogram.types import FSInputFile
from os import getenv
import os
import logging 
import random

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command ("start"))
async def start_handler(message: types.Message):
    print("Message", message)
    print("Userinfo", message.from_user)
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}")

@dp.message(Command ("my_info"))
async def my_info_handler(message: types.Message):
    await message.answer(f"Информация о вас \n Имя: {message.from_user.first_name}\n Ваш ник:{message.from_user.username} \n Ваш id: {message.from_user.id} ")

@dp.message(Command("photo"))
async def picture_handler(message: types.Message):
    random_photo = random.choice(os.listdir('images'))
    photo = FSInputFile(f'images/{random_photo}')
    await message.reply_photo(photo, caption = 'Рандомная фотка')

@dp.message()
async def echo_handler(message: types.Message):
    await message.reply(message.text)

async def main():
    # запускаем бот
   await dp.start_polling(bot)
   

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

