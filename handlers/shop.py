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
async def show_books(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    meals = message.text.capitalize()
    caffe = await database.fetch("""
        SELECT * FROM caffe 
        INNER JOIN meals ON caffe.meals_id = meals.id
        WHERE meals.name = ?
    """, (meals,))
    # print(caffe)
    await message.answer(f"Блюдо по выбору: {meals}", reply_markup=kb)
    for caffe in caffe:
        photo = types.FSInputFile(caffe["images"])
        await message.answer_photo(
            photo=photo,
            caption=f"{caffe['name']} - {caffe['price']} сом"
        )