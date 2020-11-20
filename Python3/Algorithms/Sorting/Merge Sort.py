from array import array

# Note: I've read that this method is much more effective for linkedlists
# I suspect that doing this with arrays is rather silly
#   If this exercise turns out to be only for arrays, I'll do it again using them

# input will be an unsorted line of space-separated integers from -100000 to 100000 (could be larger)
#   (e.g. 1 4 3 5 6 2 8)
list_to_be_sorted = list(map(int, input().split()))

left_index = 0
# Find the middle point to divide the array into two halves
# if the length of the array is odd, then the left array will have one more element than the right array
middle_index = len(list_to_be_sorted) // 2
right_index = len(list_to_be_sorted)


def merge_sort(lst, middle_index, right_index):

    new_sub_list = list()
    if len(lst) <= 1:
        # if the list is just one element long, return it
        return lst

    else:
        # base case: list is length 2
        #   sort the two elements
        if len(lst) == 2:
            left_element = lst[0]
            right_element = lst[1]
            if left_element <= right_element:
                new_sub_list.append(left_element)
                new_sub_list.append(right_element)
            else:
                new_sub_list.append(right_element)
                new_sub_list.append(left_element)
            return new_sub_list


        else:
            # declare new list and indices, for clarity
            temp_new_list = lst[:middle_index]
            temp_new_middle_index = len(temp_new_list) // 2
            temp_new_end_index = len(temp_new_list)

            # recursive call to merge-sort
            left_list = merge_sort(temp_new_list, temp_new_middle_index, temp_new_end_index)

            # declare new list and indices, for clarity
            temp_new_list = lst[middle_index:right_index]
            temp_new_middle_index = len(temp_new_list) // 2
            temp_new_end_index = len(temp_new_list)

            # recursive call to merge-sort
            right_list = merge_sort(temp_new_list, temp_new_middle_index, temp_new_end_index)


            # since the merge sort has been recursively called
            # we can assume that the left hand side and right hand list have been sorted

            # now we build a new list from left to right of both lists simultaneously
            # i is the index for elements on the LHS
            # j is the index for elements on the RHS
            i = 0
            j = 0
            while(len(new_sub_list) < len(left_list) + len(right_list)):
                # if we have reach the end of the left list,
                #   extend the rest of the right list onto result
                if len(left_list) == i:
                    new_sub_list.extend(right_list[j:len(right_list)])
                    break

                # if we have reach the end of the right list,
                #   extend the rest of the left list onto result
                elif len(right_list) == j:
                    new_sub_list.extend(left_list)
                    break
                else:
                    # traverse the list and append the smallest element at a time
                    #   since both sides have been sorted, already we can proceed
                    if left_list[i] <= right_list[j]:
                        new_sub_list.append(left_list[i])
                        i += 1
                    else:
                        new_sub_list.append(right_list[j])
                        j += 1


    return new_sub_list



print(merge_sort(list_to_be_sorted, middle_index, right_index))