my_tuple = tuple(input('Введите строку: '))
counter = 0
for i in my_tuple:
    if i.isalpha():
        counter+=1
print(f'Количество букв в строке: {counter}')

