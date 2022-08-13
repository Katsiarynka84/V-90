word_1 = input('Введите первое слово: ')
word_2 = input('Введите второе слово: ')
list_1 = [i for i in word_1]
list_1.sort()
list_2 = [i for i in word_2]
list_2.sort()
if list_1 == list_2:
    print("Анаграмма")
else:
    print('Это не анаграмма')
