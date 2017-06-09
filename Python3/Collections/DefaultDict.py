from collections import defaultdict

first_input = list(map(int, input().split()))
n = first_input[0]
m = first_input[1]

word_groups = defaultdict(list)
for _ in range(n):
    word_groups['A'].append(input().split(' '))
for _ in range(m):
    word_groups['B'].append(input().split(' '))


for m_value in word_groups['B']:
    # create new list to store indices
    indices = []
    # create index (defaultdictionary is unordered, thus we need to make indexes manually)
    index = 1
    for n_value in word_groups['A']:
        if m_value == n_value:
            indices.append(index)
        index += 1

    if len(indices) == 0:
        print(-1)
    else:
        for indx in indices:
            print(indx, end=" ")
        print()
