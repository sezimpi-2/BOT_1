from aiogram import Router, F, types
from aiogram.filters.command import Command


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


@shop_router.message(F.text == "Пиццы")
async def show_fantastika(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Виды пицц", reply_markup=kb)


@shop_router.message(F.text == "Пасты")
async def show_romantika(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Виды паст", reply_markup=kb)


@shop_router.message(F.text == "Напитки")
async def show_drama(message: types.Message):
    
    await message.answer("Виды напитков")