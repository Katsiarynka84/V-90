with open('poem.txt', encoding='utf-8') as poem:
    text = poem.read()
    count_gl = 0
    count_sogl = 0
    for i in text:
        if i.lower() in 'аяоёуюыиэе':
            count_gl += 1
        else:
            count_sogl += 1
    print(text, '\n')
    if count_sogl == count_gl:
        print(f'Равное количество гласных и согласных букв: {count_sogl}')
    else:
        print((f'Согласных букв больше, чем гласных  {count_sogl}:{count_gl}',
           f'Гласных букв больше, чем согласных  {count_gl}:{count_sogl}')
          [count_gl > count_sogl]
           )
# text = '''Однажды в студеную зимнюю пору
# Я из лесу вышел. Был сильный мороз.
# Гляжу, поднимается медленно в гору
# Лошадка, везущая хворосту воз.'''
# count_gl = 0
# count_sogl = 0
# for i in text:
#     if i.lower() in 'аяоёуюыиэе':
#         count_gl += 1
#     else:
#         count_sogl += 1
# print(count_sogl, count_gl)