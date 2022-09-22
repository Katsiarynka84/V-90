with open('file.txt') as my_file:
    print(f'Количество строк в файле: {len(my_file.readlines())}')

    my_file.seek(0)
    text = my_file.read()
    #print(text)
    my_list = []
    word = ''
    counter = 0

    for i in text:
        if not i.isalpha():
            if word:
                my_list.append(word)
                word = ''
        else:
            counter += 1
            word += i
# print(my_list)
print(f'Количество букв в тексте: {counter}\nКоличество слов в тексте: {len(my_list)}')
