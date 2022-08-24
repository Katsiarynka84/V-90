list1 = [3, 5, 7, 'jo']
list2 = [6, 'jo', 3, 9, 5, 7]
list3 = []
if len(list1) < len(list2):
    list1, list2 = list2, list1
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
print(list3)




