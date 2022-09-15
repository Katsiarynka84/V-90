s = [234, 'asdf', [3, 3]]
my_set = set()
for i in s:
    try:
        my_set.add(i)
    except TypeError:
        pass
print(my_set)




