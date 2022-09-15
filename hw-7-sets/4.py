#list1 = [int(i) for i in input('Введите элементы первого списка через пробел:')]
try:
    list1 = [int(i) for i in input('Введите элементы списка через пробел: ').split()]
except ValueError:
    print('В списке допустимы только натуральные числа.')

else:
    my_set = set()
    for i in list1:
        if i in my_set:
            continue
        elif list1.count(i) == 1:
            my_set.add(i)
        else:
            my_set.add(i)
            for j in range(1, list1.count(i)):
                my_set.add(str((str(i)*(j+1))))
    print(my_set)


