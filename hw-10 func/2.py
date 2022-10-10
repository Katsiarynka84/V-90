
def main():
    def abracadabra(a, name: str, num1: int, num2: int, language='Python', year=1992):
        return f'{name} ({num1} + {num2} - {a}) / 3 {language}, {year}'

    def inspect_function(f):
        print(f'Имя функции: {f.__name__}')
        print(f'Аргументы по умолчанию: ', *f.__defaults__)
        print('Ключевые аргументы: ', end='')
        for i, j in f.__annotations__.items():
            print(f'{i}: {j}', end=', ')

    inspect_function(abracadabra)


if __name__ == '__main__':
    main()
