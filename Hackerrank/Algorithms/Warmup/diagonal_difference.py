def diagonalDifference(arr):
    sum_left = 0
    sum_right = 0
    for i, nested_arr in enumerate(arr):
        sum_left += nested_arr[i]
        sum_right += nested_arr[len(arr)-1-i]

    diff = sum_left - sum_right
    return -diff if diff < 0 else diff



if __name__ == '__main__':
    n = diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
    print(n)