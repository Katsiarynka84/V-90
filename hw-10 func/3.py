def main():
    def pangr(s):
        import string
        return 'Строка-панграмм!' if set(string.ascii_lowercase).issubset(set(s.lower())) else 'Это не панграмм!'
    print(pangr(input(f'Введите строку: \n')))


if __name__ == '__main__':
    main()
