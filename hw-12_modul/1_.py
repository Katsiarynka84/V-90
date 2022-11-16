from decimal import Decimal
s = '2.45 2.69 2.45 3.45 2.00 0.04 7.25'
my_list = [Decimal(i) for i in s.split()]
print(sum(my_list))
print(*[float(i) for i in sorted(my_list)])