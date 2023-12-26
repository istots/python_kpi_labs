print('Discount table')
product_list = [15.89, 39.99, 82.10, 135.85, 18.90, 510.00, 799.98]
for product in product_list:
    print("{0} {1} {2}".format(product, round(product*0.6, 2), round(product-round(product*0.6, 2), 2)))
