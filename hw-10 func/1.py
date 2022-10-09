def main():
    def sum_range(start, end):
        if start > end:
            start, end = end, start
        return sum(range(start, end + 1))
    try:
        print(sum_range(int(input('Введите первое число: ')), int((input('Введите второе число: ')))))
    except ValueError:
        print('Вы ввели не число.')


if __name__ == '__main__':
    main()
