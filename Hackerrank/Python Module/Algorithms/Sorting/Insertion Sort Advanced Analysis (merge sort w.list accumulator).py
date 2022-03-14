

test_cases = int(input())

class Accumulator():
    def __init__(self):
        self.sum = 0

    def __add__(self, number):
        self.sum += number
        return self.sum

count = Accumulator().__init__()

def merge_sort_count(lst, count2):
    if len(lst) == 1:
        return lst

    elif len(lst) == 2:
        if lst[0] > lst[1]:
            temp = lst[0]
            lst[0] = lst[1]
            lst[1] = temp
            count2.append(1)
            return lst
        else:
            return lst

    middle_index = len(lst) // 2
    left_side = merge_sort_count(lst[:middle_index], count2)
    right_side = merge_sort_count(lst[middle_index:len(lst)], count2)

    result = []
    i = 0
    j = 0
    while(len(result) < len(left_side) + len(right_side)):
        if i == len(left_side):
            result.extend(right_side[j:len(right_side)])
            break
        elif j == len(right_side):
            result.extend(left_side[i:len(left_side)])
            break
        else:
            if left_side[i] <= right_side[j]:
                result.append(left_side[i])
                i += 1
            else:
                result.append(right_side[j])
                j += 1
                count2.append(len(left_side) - i)
    if len(result) == size:
        return sum(count2)
    else:
        return result




for _ in range(test_cases):
    size = int(input())

    full_list = list(map(int, input().split()))

    count = Accumulator().sum
    count2 = [0]

    print(merge_sort_count(full_list, count2))
