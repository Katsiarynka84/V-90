s = input("Введите строку: ")
a = input("Введите символ: ")
if a.lower() not in s.lower():
    print('Символ отсутствует в данной строке.')
else:
    print(f'Количество вхождений символа в стрку: {s.lower().count(a.lower())}')