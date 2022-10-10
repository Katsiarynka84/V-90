import random
import string


def main():
    def pangr(s):
        import string
        return f'"{s}" Строка-панграммa!' if set(string.ascii_lowercase).issubset(set(s.lower())) \
            else f'Это "{s}" не панграммa!'

    a = list(string.ascii_letters)
    random.shuffle(a)
    print(pangr(''.join(a)))
    b = ''.join(random.sample(string.ascii_letters+string.digits, 40))
    print(pangr(b))
    print(pangr((input(f'Введите строку: \n'))))


if __name__ == '__main__':
    main()
