import asyncio
import logging 
from config import dp, bot
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.photo import photo_router
from handlers.my_info import info_router
from handlers.survey import survey_router
from handlers.shop import shop_router


async def main():
#    регистрируем роутер
  
   dp.include_router(start_router)
   dp.include_router(photo_router)
   dp.include_router(info_router)
   dp.include_router(echo_router)
   dp.include_router(survey_router)
   dp.include_router(shop_router)



    # запускаем бот

   await dp.start_polling(bot)
   

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

