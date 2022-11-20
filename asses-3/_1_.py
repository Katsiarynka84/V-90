from random import randint
my_list = [randint(1, 1000) for i in range(10)]
for i in filter(lambda n: n % 15 == 0, my_list):
    print(i, end=' ')

