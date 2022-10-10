def main():
    mylist = [3, 0, 5, True, 'kjhg']

    def to_set(a):
        return set(filter(lambda x: isinstance(x, (int, str, tuple, bool)), a))

    print(to_set(mylist))


if __name__ == '__main__':
    main()
