with open('file.txt') as text:
    lat = 0
    lines = 0
    for line in text.readlines():
        lines += 1
        for symb in line:
            if 91 > ord(symb.upper()) > 64:
                lat += 1
    print('Количество латинских букв в тексте:', lat)
    print("Количество строк в тексте:", lines)

