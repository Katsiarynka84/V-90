s = input('Введите элементы списка через пробел:\n').split()
list1 = []
for i in s:
    if s.count(i) > 1:
        list1.append(i)
        s.remove(i)
print(list1)