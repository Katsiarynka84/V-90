def main():

    def func_gener(a, b, c=0):
        if a > b:
            a, b = b, a

        for num in range(a, b+1, c):
            yield num

    while True:
        try:
            x, y, z = (int(i) for i in input('Введите данные через пробел:\n').split())
            my_gener = func_gener(x, y, z)

            for i in my_gener:
                print(i, end=' ')
            break
        except ValueError:
            print('Вы ввели не число либо дробное число.'
                  'Третье значение должно быть больше "0"\n'
                  'Введите 3 целых числа/n')


if __name__ == '__main__':
    main()
