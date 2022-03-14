def has_cycle(head):
    curr_node_slow = head
    curr_node_fast = head.next
    while curr_node_fast and curr_node_slow:
        if id(curr_node_fast) == id(curr_node_slow):
            return 1
        elif curr_node_fast.next:
            curr_node_slow = curr_node_slow.next
            curr_node_fast = curr_node_fast.next.next
        else:
            return 0
