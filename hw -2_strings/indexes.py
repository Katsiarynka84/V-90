s = input('Введите строку: ')
print(f'Третий символ строки: {s[2]}')
print(f'Предпоследний символ строки:  {s[-2]}')
print(f'Первые пять символов строки:  {s[:5]}')
print(f'Строка без последних двух символов:  {s[:-2]}')
print(f'Символы с четными индексами:  {s[::2]}')
print(f'Символы с нечетными индексами:  {s[1::2]}')
print(f'Символы в обратном порядке:  {s[::-1]}')
print(f'Символы строки через один в обратном порядке:  {s[::-2]}')
