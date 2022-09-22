with open('file.txt') as my_file:
    line_counter = 0
    lines = my_file.readlines()
    for i in lines:
        if len(i) > 1:
            line_counter += 1
    print(f'Количество  заполненных строк в файле: {line_counter}')
    print(f'Количество пустых строк в файле: {len(lines)-line_counter}')

    my_file.seek(0)
    text = my_file.read()
    # print(text)
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
