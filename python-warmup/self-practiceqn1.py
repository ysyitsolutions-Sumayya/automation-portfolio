number_list = []
for number in range(2000, 3200):
    if number % 7 == 0 and number % 5 != 0:
        number_list.append(str(number))
    print(','.join(number_list))