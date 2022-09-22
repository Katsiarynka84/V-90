import os
file_list = os.listdir()

my_list = []
request = input('Введите запрос: ').lower()

for file in file_list:
    with open(file, encoding='utf-8') as curr_file:
        text = curr_file.read()
        if request in text.lower():
            my_list.append(file)
if my_list:
    print(f'Искомое слово встречается в следующих файлах: {", ".join(my_list)}')
else:
    print(f'Искомый элемент "{request}" не найден')
