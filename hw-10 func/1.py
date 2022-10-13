def main():
    def sum_range(start, end):
        '''Функция возвращает сумму чисел в диапазоне от start до end включительно'''
        if start > end:
            start, end = end, start
        return f'Сумма элементов в диапазоне {start}:{end} равна {sum(range(start, end + 1))}'

    while True:
        try:
            print(sum_range(int(input('Введите первое число: ')), int((input('Введите второе число: ')))))
            break
        except ValueError:
            print('Вы ввели не число. Попробуйте еще раз.\n')


if __name__ == '__main__':
    main()
