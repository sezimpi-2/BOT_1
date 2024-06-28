from aiogram import Router, types
from aiogram.filters.command import Command
from crawler.house_kg import get_page, get_links

house_router = Router()

@house_router.message(Command("obyavleniya"))
async def show_obyavlenia(message: types.Message):
    page = get_page()
    links = get_links(page)
    if links:
        for link in links:
            await message.answer(link)
    else:
        await message.answer("Не удалось получить ссылки на объявления.")