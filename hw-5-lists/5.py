list = [1, 4, 7, 3, 9, 5, 9, 3]
ind1 = list.index(min(list))
ind2 = list.index(max(list))
list[ind1], list[ind2] = list[ind2], list[ind1]
print(list)