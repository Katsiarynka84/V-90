cockt_list = {'marg': 7, 'bely': 8, 'b52': 13, 'mery': 9, 'sex': 10}

try:
    money = int(input('Введите сумму: '))
    flag = True
    for drink, price in cockt_list.items():
        if money > cockt_list[drink]:
            flag = False
            print(drink, price)
    if flag:
        print('Вы не заработали на коктейль :(((')

except ValueError:
    print('Необходимо ввести число')