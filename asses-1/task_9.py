s = [i for i in input().split()]
my_list = []
for i in s:
    num = ''
    for j in range(len(i)):
        if i[j].isdigit():
            num += i[j]
    if len(num) > 0:
        my_list.append(num)
print(my_list)