from math import sqrt
import time


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        do = func(*args, **kwargs)
        end = time.perf_counter()
        work_time = end - start
        print(f'Время выполнения функции "{func.__name__}": {round(work_time, 4)} сек.')
        return do
    return wrapper


@timing
def length(a, b, c, d):
    pif = sqrt(((a - b)**2+(c - d)**2))
    return f'Длина отрезка равна {pif}'


while True:
    try:
        x1, y1, x2, y2 = float(input('введите 4 числа:\n')), float(input()), float(input()), float(input())
        print(length(x1, y1, x2, y2))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте еще раз")
