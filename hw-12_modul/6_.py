from itertools import filterfalse
my_list = (4.6, -7, 15, 67, -7.60)
new_list = tuple(filterfalse(lambda n: type(n) is int and n >= 0, my_list))
print(*new_list)
