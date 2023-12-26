product_list = [29.25, 48.99, 99.98, 124.665, 214.30, 543.90, 799.85]
discount_list = []
new_price_list = []

def disc_table(param, function):
    return function(param)

def discount(num):
    return num * 0.6

def new_price(num):
    return num - (num * 0.6)

print('Discount table')

for prod in product_list:
    new_price_list.append(round(disc_table(prod, new_price), 2))
    discount_list.append(round(disc_table(prod, discount), 2))
    print("{0} {1} {2}".format(prod, round(disc_table(prod, new_price), 2), round(disc_table(prod, discount), 2)))