import functools


def main():
    from math import sqrt
    import time

    def timing(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            do = func(*args, **kwargs)
            end = time.perf_counter()
            work_time = end - start
            print(f'Время выполнения функции "{func.__name__}": {round(work_time, 4)} сек.')
            return do
        return wrapper

    @timing
    def length(a: int, b: int, c: int, d: int):
        '''Функция вычисляет длину отрезка
        на плоскости по 2м координатам'''
        pif = sqrt(((a - b)**2+(c - d)**2))
        return f'Длина отрезка равна {round(pif, 4)}'

    while True:
        try:
            x1, y1, x2, y2 = int(input('введите 4 числа:\n')), int(input()), int(input()), int(input())
            print(length(x1, y1, x2, y2))
            break
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз")


if __name__ == '__main__':
    main()
