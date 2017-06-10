from collections import deque

d = deque()
for _ in range(int(input())):
    line_input = input().split()
    command = line_input[0]
    # getattr() doesn't work for pop or popleft (with or without brackets)
    if command == "pop":

        d.pop()
    elif command == "popleft":
        d.popleft()
    else: getattr(d, command)(line_input[-1])

for element in d:
    print(element, end=" ")
