from array import array

size = int(input())

# set up array
insertion_sort_array_1 = array('i', list(map(int, input().split())))

def print_array(ary):
    for i in range(len(ary)):
        print(ary[i], end=" ")
    print()




# refactored for starting index to be passed from second insertion_sort method
# and go until we reach the 0th element (down to, but not including, -1)
def insertion_sort_1(ary, starting_index, key_index):
    key = insertion_sort_array_1[key_index]
    for j in range(starting_index, -1, -1):

        # since this is python, we have to be careful with the index
        #   if we index the list at -1, this means the index will start checking the end of the list
        if key < ary[j]:
            ary[j+1] = ary[j]
        else:
            ary[j+1] = key
            break
        print_array(ary)

        if j == 0:
            ary[j] = key

    print_array(ary)

insertion_sort_1(insertion_sort_array_1, size - 2, size - 1)
