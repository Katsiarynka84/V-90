s, charr = input('Введите строку: '), input('Введите символ: ')
if s.count(charr) == 0:
    print(f'Cимвол "{charr}" не найден.')
else:
    print(f'Найден только один искомый символ. Индекс вхождения: {s.find(charr)}.'if s.count(charr) == 1 else
          f"Первое вхождение символа '{charr}' с индексом {s.find(charr)}. "
          f"Последнее вхождение символа '{charr}' с индексом {s.rfind(charr)}.")


