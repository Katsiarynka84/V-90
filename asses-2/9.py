list = [4, 67, '33', 3, 0, '67', '99.4']

while True:
    try:
        a = float(input('Введите число: '))
    except ValueError as m:
        print(f'Ошибка {m}. Вы ввели не число')
    for i in list:
        try:
            print(a / float(i))
        except ValueError as v:
            print(f'{v}. Неверное значение')
        except ZeroDivisionError as d:
            print(f'Ошибка {d}. Делить на ноль нельзя')
            break

    break

