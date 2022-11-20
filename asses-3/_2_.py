def calcul(a, b):
    return f'Сумма чисел:', a + b, '\nPaзность чисел:', a - b


print(*calcul(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
