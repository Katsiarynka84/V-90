s = [3, 'sdf', 65, 'sdf', 14, 3]
new_list = []
for i in s:
    if s.count(i) > 1 and i not in new_list:
        new_list.append(i)
print('Повторяющиеся элементы: ', *new_list)