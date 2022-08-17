s, charr = input('Введите строку: '), input('Введите символ: ')
print(f'Количество вхождений символа "{charr}" в строку: {len([i for i in s if i == charr])}')