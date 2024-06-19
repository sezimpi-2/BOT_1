from aiogram import Router, F, types
from aiogram.filters.command import Command
import sqlite3


shop_router = Router()


@shop_router.message(Command("shop"))
async def show_shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Пиццы"),
            ],
            [
                types.KeyboardButton(text="Пасты"),
                types.KeyboardButton(text="Напитки"),
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите блюдо:", reply_markup=kb)

meals = ("пиццы", "напитки", "пасты")


@shop_router.message(F.text.lower().in_(meals))
async def show_caffe(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    meals = message.text # одно из meals
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    query = cursor.execute("SELECT * FROM caffe WHERE meals_id = 1")
    caffe = query.fetchall()
    print(caffe)
    await message.answer("Блюда по выбору: ", reply_markup=kb)