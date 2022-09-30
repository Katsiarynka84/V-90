s = (5, 6, '1', '2', '2', '3', '3', '3', '4', '4')
# try:
#     ss = [int(i) for i in s]
#     print(tuple(sorted(ss)))

try:
    print(*sorted(map(int, s)))
except ValueError:
    print('ошибка', s)
