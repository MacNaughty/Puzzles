def GetNode(head, position):
    curr_node = head
    list_of_data = []
    while curr_node:
        list_of_data.append(curr_node.data)
        curr_node = curr_node.next
    return list_of_data[len(list_of_data) - 1 - position]
