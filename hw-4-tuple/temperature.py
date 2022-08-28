temperature = tuple([int(i) for i in input('Введите данные через пробел: ').split()])
print(f'Средняя температура: {sum(temperature) / len(temperature)}')
