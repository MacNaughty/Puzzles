from array import array

size = int(input())

# set up array
insertion_sort_array_1 = array('i', list(map(int, input().split())))

def print_array(ary):
    for i in range(len(ary)):
        print(ary[i], end=" ")
    print()

key = insertion_sort_array_1[size - 1]
j = size - 1
# we start our loop from the second to last element (size - 2)
# and go until we reach the 0th element (down to, but not including, -1)
for j in range(size - 2, -1, -1):
    # since this is python, we have to be careful with the index
    #   if we index the list at -1, this means the index will start checking the end of the list
    if key < insertion_sort_array_1[j]:
        insertion_sort_array_1[j+1] = insertion_sort_array_1[j]
    else:
        insertion_sort_array_1[j+1] = key
        break
    print_array(insertion_sort_array_1)

    if j == 0:
        insertion_sort_array_1[j] = key

# print solution
print_array(insertion_sort_array_1)
