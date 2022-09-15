set1 = {i for i in input("Введите элемены множества set1 через пробел: ").split()}
set2 = {i for i in input("Введите элемены множества set2 через пробел: ").split()}

if set2 == set1:
    print('Множества равны.')
elif set1 > set2:
    print('set1 является чистым супермножеством set2.')
elif set2.issuperset(set1):
    print('set2 является чистым супермножеством set1.')
else:
    print('Супермножество не обнаружено :(')
