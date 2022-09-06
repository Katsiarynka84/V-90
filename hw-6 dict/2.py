dict1 = {'a': 300, 5: 25.52, 'd': 4}
dict2 = {5: 2, 'a': 3, 'c': 17}
if dict1 == dict2:
    dict3 = {i: dict1[i] * dict2[i] for i in dict2}
    print(dict3)
else:
    dict3 = {i: dict1[i] * dict2[i] for i in dict2 if i in dict1}
    dict2.update(dict3)
    dict1.update(dict2)
    print(dict1)
