from aiogram import Router, F, types
from aiogram.filters.command import Command
from crawler.house_kg import get_page, get_links


house_router = Router()


@house_router.message(Command("obyavlenia"))
async def show_obyavlenia(message: types.Message):
    await message.answer("Чтобы посмтреть обьявления нажмите на \n https://www.house.kg/snyat ")