s = ['d', '    ', 'dfdsdf', '23', '']
for i in s:
    if i.isspace() or i == '':
        s.remove(i)
print(s)