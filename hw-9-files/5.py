numbers = [i for i in input('Введите числа через пробел: ').split()]
with open ('number_list.txt', 'w') as doc:
    for i in numbers:
        print(i, file=doc)

try:
    with open('number_list.txt', 'r+') as doc:
        print(doc.read())
        doc.seek(0)
        mult = 1
        summa = 0
        for i in doc.readlines():
            try:
                summa += float(i)
                mult *= float(i)
            except ValueError as d:
                print('Все введенные значения должны быть числами', d)
        print(summa, mult, sep='\n', file=doc)
except Exception as e:
    print('ошибка при чтении файла', e)