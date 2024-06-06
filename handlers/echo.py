from aiogram import Router, types


echo_router=Router()


@echo_router.message()
async def echo_handler(message: types.Message):
    await message.reply('Я не понимаю вас.\n Вот команды которые я понимаю: \n /start \n /photo \n /my_info \n /echo')
