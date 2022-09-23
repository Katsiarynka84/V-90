numbers = [i for i in input('Введите числа через пробел: ').split()]
with open ('number_list.txt', 'w') as doc:
    for i in numbers:
        print(i, file=doc)
with open('number_list.txt') as doc:
    print(doc.read())
