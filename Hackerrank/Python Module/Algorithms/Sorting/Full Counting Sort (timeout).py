size = int(input())
list_of_dictionaries = list()
for number in range(0, size // 2):
    temp_list = list(input().split())
    temp_dict = {int(temp_list[0]): '-'}
    list_of_dictionaries.append(temp_dict)

for number in range(size // 2, size):
    temp_list = list(input().split())
    temp_dict = {int(temp_list[0]): temp_list[1]}
    list_of_dictionaries.append(temp_dict)


for i in range(100):
    for dictionary in list_of_dictionaries:
        if i in dictionary:
            print(dictionary[i], end=" ")
