from collections import *
from sys import maxsize

number_of_test_cases = int(input())

for _ in range(number_of_test_cases):
    number_of_cubes = int(input())
    cube_deque = deque(map(int, input().split()))

    result = "Yes"
    last_cube_in_pile = maxsize


    for _ in range(number_of_cubes):
        leftmost_cube_length = cube_deque[0]
        rightmost_cube_length = cube_deque[-1]

        if leftmost_cube_length >= rightmost_cube_length:
            if leftmost_cube_length <= last_cube_in_pile:
                last_cube_in_pile = cube_deque.popleft()
            else:
                result = "No"
                break

        elif rightmost_cube_length <= last_cube_in_pile:
            last_cube_in_pile = cube_deque.pop()

        else:
            result = "No"
            break

    print(result)
