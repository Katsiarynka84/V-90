text = open('file.txt')
print("Количество строк в тексте:", len(text.readlines()))
lat = 0
text.seek(0)
for i in text.read():
    if 91 > ord(i.upper()) > 64:
        lat += 1
print('Количество латинских букв в тексте:', lat)
