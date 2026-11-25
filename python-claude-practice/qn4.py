# qn4
orders = [
    {'customer': 'Ali', 'total': 100},
    {'customer': 'Sara', 'total': 150},
    {'customer': 'Ali', 'total': 200},
    {'customer': 'John'},
]

dict_orders = {}
for order in orders:
    customer = order['customer']
    total = order['total']
    if customer in dict_orders:
        dict_orders[customer] += total
    else:
        dict_orders[customer] = total

print(dict_orders)