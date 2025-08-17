def equal(arr):

    min_heap = []
    max_heap = []
    for num_chocolates in arr:
        heappush(min_heap, num_chocolates)
        heappush(max_heap, -num_chocolates)

    res = 0

    min_chocolates = min_heap[0]
    max_chocolates = max_heap[0]
    diff = max_chocolates - min_chocolates
    while diff > 0:
        if diff >= 5:
            num_chocolates = 5
        elif diff >= 2:
            num_chocolates = 2
        else:
            num_chocolates = 1

        for i in range(len(arr) - 1):
            arr[i] += num_chocolates

        for i in range(len(arr)-1, 0, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
            else:
                break

        diff = arr[-1] - arr[0]
        res += 1

    return res