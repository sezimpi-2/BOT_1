from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from aiogram.types import FSInputFile
from os import getenv


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

