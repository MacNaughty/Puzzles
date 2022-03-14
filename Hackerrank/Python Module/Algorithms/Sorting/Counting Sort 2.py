from collections import Counter

size = int(input())
list_to_be_counted = list(map(int, input().split()))

counted_list = Counter(list_to_be_counted)

for number in range(size):
    for current_number in range(counted_list[number]):
        print(number, end=" ")
