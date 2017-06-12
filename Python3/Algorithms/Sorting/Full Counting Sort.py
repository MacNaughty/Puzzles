size = int(input())

master_dictionary = dict()
for key in range(100):
    master_dictionary[key] = []

for number in range(0, size // 2):
    temp_list = list(input().split())
    master_dictionary[int(temp_list[0])].extend(['-'])


for number in range(size // 2, size):
    temp_list = list(input().split())
    master_dictionary[int(temp_list[0])].extend([temp_list[1]])


for key, values in master_dictionary.items():
    for value in values:
        print(value, end=" ")
