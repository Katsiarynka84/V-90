list1 = set([int(i) for i in input('Введите элементы первого списка через пробел: ').split()])
list2 = set([int(i) for i in input('Введите элементы второго списка через пробел: ').split()])
print(*sorted(list1 & list2))