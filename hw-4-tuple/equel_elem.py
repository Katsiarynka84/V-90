tuple1 = (3, 3, 5, True, 'mu', [])
tuple2 = (9, 'tu', [], 3, False, 9, True, 5, 7)
my_list = []
for i in tuple1:
    for j in tuple2:
        if i == j and i not in my_list:
            my_list.append(i)
            break

print('Одинаковые элементы: ', *my_list)
print(f'Одинаковые элементы: {my_list}')
print('Одинаковые элементы: ', *my_list, sep=',')
print(f'Одинаковые элементы: {", ".join(map(str, my_list))}')

# если указать разделитель sep=',' то поставит запятую и после текста
# если все в ф-строку - не получается быстро распаковать список
# хотелось бы, чтобы ф-строкой и элементы через запятую




