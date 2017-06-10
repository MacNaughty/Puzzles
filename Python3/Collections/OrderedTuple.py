from collections import *

number_of_items = int(input())
item_name_and_price = OrderedDict()

for _ in range(number_of_items):
    line_input = input().split()
    item_name = " ".join(line_input[:-1])
    if item_name in item_name_and_price:
        item_name_and_price[item_name] += int(line_input[-1])
    else: item_name_and_price[item_name] = int(line_input[-1])

for item in item_name_and_price:
    print(item + " " + str(item_name_and_price[item]))
