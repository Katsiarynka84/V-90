import functools


def main():

    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            do = func(*args, **kwargs)
            print('Ваша последовательность готова:')
            return do
        return wrapper

    @decor
    def func_gener(a, b, c=0):
        '''Функция генерирует последовательность от "а" до "b" включительно
        с шагом "с".'''
        if a > b:
            a, b = b, a
        try:
            for num in range(a, b+1, c):
                yield num
        except ValueError:
            print('Третье значение должно быть больше "0"')

    while True:
        try:
            x, y, z = (int(i) for i in input('Введите данные через пробел:\n').split())
            if z == 0:
                print('Третье значение должно быть больше "0"')
                continue
            my_gener = func_gener(x, y, z)
            for i in my_gener:
                print(i, end=' ')
            break
        except ValueError:
            print('Вы ввели не число либо дробное число. Введите 3 целых числа\n')


if __name__ == '__main__':
    main()
