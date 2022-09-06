my_list = []
my_list.extend(input('Введите строку: '))
my_dict = {i: my_list.count(i) for i in my_list if i.isalpha()}
print(my_dict)