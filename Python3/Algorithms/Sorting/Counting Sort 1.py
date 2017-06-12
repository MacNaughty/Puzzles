from collections import Counter

size = int(input())
list_to_be_counted = list(map(int, input().split()))

counted_list = Counter(list_to_be_counted)

for number in range(100):
    print(counted_list[number], end=" ")
