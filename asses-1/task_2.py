list1 = [1, 2, 3]
list2 = [11, 22, 33]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
print(list3)