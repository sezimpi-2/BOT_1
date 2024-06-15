import asyncio
import logging 
from aiogram import types
from config import dp, bot, database
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.photo import photo_router
from handlers.my_info import info_router
from handlers.survey import survey_router
from handlers.shop import shop_router


async def on_startup(bot):
    await database.create_tables()


async def main():
   await bot.set_my_commands([
       types.BotCommand(command= 'start', description='начало'),
       types.BotCommand(command= 'my_info', description='информация'),
       types.BotCommand(command='shop', description='Наши товары'),
       types.BotCommand(command='photo', description='Фото'),
       types.BotCommand(command='opros', description='Оставить отзыв '),
      
   ])
#    регистрируем роутер
  
   dp.include_router(start_router)
   dp.include_router(photo_router)
   dp.include_router(info_router)
   dp.include_router(survey_router)
   dp.include_router(shop_router)

   dp.include_router(echo_router)


   dp.startup.register(on_startup)
    # запускаем бот

   await dp.start_polling(bot)
   

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

