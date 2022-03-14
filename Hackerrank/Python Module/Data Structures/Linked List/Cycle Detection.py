def has_cycle(head):
    curr_node = head
    index = 0
    while curr_node and index < 101:
        curr_node = curr_node.next
        index += 1
    if index != 101:
        return 0
    else:
        return 1
