import asyncio
from time import  perf_counter

async def cook_pasta():
    print("готовлю пасту")
    await asyncio.sleep(7)
    print("Готово")
    return "Паста готова"

async def cook_souce():
    print("готовлю соус")
    await asynciio.sleep(4)
    print("Соус готов")
    return "Соус готов"

async def set_table():
    print("Накрываю стол")
    await asyncio.sleep(2)
    print("Накрыла стол")
    return "Стол накрыт"


def prepare_lunch():
    pasta_task= asyncio.create_task(cook_pasta())
    souce_task = asyncio.create_task(cook_souce())
    table_task = asyncio.create_task(set_table())


    results = asyncio.gather (pasta_task, souce_task, table_task)
    print("Обед готов", *results)

if __name__ == "__main__":
    asyncio.run(prepare_lunch())
    start = perf_counter()
    prepare_lunch()
    time_taken = perf_counter()-start
    print("Все заняло ", time_taken,"с")