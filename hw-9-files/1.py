with open('prices.txt', 'r+') as price:
    total_price = (sum([int(i.strip().split()[2]) for i in price.readlines()]))
    print(f'\nTotal price = {total_price}', file=price)

#
# with open('prices.txt') as price:
#     price_list = []
#     for i in price.readlines():
#         if i:
#             price_list.append(int(i.strip().split()[2]))
#     print(sum(price_list))