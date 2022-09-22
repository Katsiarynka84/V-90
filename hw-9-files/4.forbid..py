with open('forbidden.txt') as forb_list:
    my_list = [i for i in forb_list.read().split()]

doc = 'file.txt'

with open(doc) as file_1:
    text = file_1.readlines()
    new_text = []

    for i in range(len(text)):
        s = text[i]

        for word in my_list:
            if word in s:
                number = text[i].count(word)
                s = s.replace(word, '*' * len(word), number)
        new_text.append(s.rstrip())

print(*new_text, sep='\n')
