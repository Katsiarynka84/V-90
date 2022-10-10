def main():
    def pangr(s):
        import string
        return 'Строка-панграммa!' if set(string.ascii_lowercase).issubset(set(s.lower())) else 'Это не панграммa!'
    print(pangr(input(f'Введите строку: \n')))


if __name__ == '__main__':
    main()
