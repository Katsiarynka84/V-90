s, charr = input('Введите строку: '), input('Введите символ: ')
if s.count(charr) == 0:
    print(f'Cимвол "{charr}" не найден.')
else:
    for i in range(len(s)):
        if s[i] == charr:
            first = i
            break
    for i in range(len(s)):
        if s[i] == charr:
            last = i
    if first == last:
        print(f'Найден только один искомый символ. Индекс вхождения: {first}.')
    else:
        print(
    f'''Первое вхождение символа '{charr}' с индексом {first}.
Последнее вхождение символа '{charr}' с индексом {last}.'''
)
