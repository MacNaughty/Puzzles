def miniMaxSum(arr):
    min = 10000000000
    max = 0

    for i in range(len(arr)):
        sum = 0
        for j in set(range(len(arr))) - {i}:
            sum += arr[j]

        if sum < min:
            min = sum
        if sum > max:
            max = sum

    print(f'{min} {max}')




if __name__ == '__main__':
    # miniMaxSum([1, 3, 5, 7, 9])
    miniMaxSum([1, 2, 3, 4, 5])
