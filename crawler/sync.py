from time import sleep, perf_counter

def cook_pasta():
    print("готовлю пасту")
    sleep(7)
    print("Готово")

def cook_souce():
    print("готовлю соус")
    sleep(4)
    print("Соус готов")

def set_table():
    print("Накрываю стол")
    sleep(2)
    print("Накрыла стол")


def prepare_lunch():
    cook_pasta()
    cook_souce()
    set_table()

if __name__ == "__main__":
    start = perf_counter()
    prepare_lunch()
    time_taken = perf_counter()-start
    print("Все заняло ", time_taken,"с")
    