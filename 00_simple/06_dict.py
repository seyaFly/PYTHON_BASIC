# coding=utf-8

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {'apple': 1, 'banana': 6}

# 字典值并运算
grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)
