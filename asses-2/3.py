s = '122333444455555666666'
result = {}
for i in set(s):
    result[i] = result.get(i, s.count(i))
print(result)
