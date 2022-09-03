s = [3, 5, 6, 7, 34, 906]
summ = 0
mult = 1
for i in s:
    summ += i
    mult *= i
print(f'Сумма элементов равна {summ}', f'Произведение элементов равно {mult}', sep='\n')
