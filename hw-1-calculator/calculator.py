
while True:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        c = input('Введите оператор: ')
        if c not in ('*/+-%!><='):
            print('Некорректный оператор')
    except ValueError:
        print('Вы ввели не число. Попробуйте еще раз.')
    else:
        break
if c == '/':
    try:
        print(a / b)
    except ZeroDivisionError:
        print('На ноль делить нельзя')
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '==':
    print(a == b)
elif c == '>=':
    print(a >= b)
elif c == '<=':
    print(a <= b)
elif c == '**':
    print(a ** b)
elif c == '!=':
    print(a != b)
elif c == '%':
    print(a % b)
elif c == '//':
    print(a //b)
else:
    print('Ошибка')

