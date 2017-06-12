from collections import Counter

size = int(input())
list_to_be_counted = list()
for number in range(size):
    temp_list = list(input().split())
    list_to_be_counted.append(int(temp_list[0]))

counted_list = Counter(list_to_be_counted)

total_occurrences = 0
for number in range(100):
    total_occurrences += counted_list[number]
    print(total_occurrences, end=" ")
