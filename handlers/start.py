import asyncio
from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from time import sleep

start_router=Router()

@start_router.message(Command ("start"))
async def start_handler(message: types.Message):
    # print("Message", message)
    # print("Userinfo", message.from_user, "Я бот кафе Tutta La Vitta")
    kb = types.InlineKeyboardMarkup( 
        inline_keyboard=[ 
            [ 
                types.InlineKeyboardButton(text="Наш сайт", url="https://tuttalavitta.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/tutta_la_vitta.kg") 
            ],
            [ 
                types.InlineKeyboardButton(text="О нас ", callback_data="about") 
            ],
             [ 
                types.InlineKeyboardButton(text="Меню", callback_data="reply_photo") 
            ],
            [ 
                types.InlineKeyboardButton(text="Адрес", url= "https://go.2gis.com/jgqs7 ")
            ],
             [ 
                types.InlineKeyboardButton(text="Отзыв", callback_data= "otzyv")
            ] 
            

        ] 
    )
    
    
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}! \n Я бот кафе 'Tutta La Vita' ",reply_markup=kb )
   

@start_router.callback_query(F.data =="about")
async def about_handler(callback: types.CallbackQuery):
    file_1 = FSInputFile("images_2/about.jpg")
    await callback.answer() 
    await asyncio.sleep(10)
    await callback.message.answer_photo(photo=file_1, caption="Ресторан итальянской кухни в винтажном стиле ")
    

@start_router.callback_query(F.data=="reply_photo")
async def reply_photo_handler(callback: types.CallbackQuery):
    file = FSInputFile("images_2/restoran.jpg")
    await callback.answer()  
    await asyncio.sleep(12)
    await callback.message.reply_photo(photo=file, caption="меню")


@start_router.callback_query(F.data =="otzyv")
async def about_handler(callback: types.CallbackQuery):
    await callback.answer() 
    await callback.message.answer("Начните опрос написав комманду /opros")
    
