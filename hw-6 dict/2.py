dict1 = {'a': 300, 5: 25.52, 'd': 4}
dict2 = {5: 2, 'a': 3, 'c': 17}
dict3 = dict1 | dict2
dict3 |= {key: dict1[key] * dict2[key] for key in dict2 if key in dict1}
print(dict3)
