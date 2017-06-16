def RemoveDuplicates(head):
    curr_node = head
    while curr_node:
        if not curr_node.next:
            break
        if curr_node.data != curr_node.next.data:
            curr_node = curr_node.next
        else:
            next_node = curr_node.next
            while next_node and next_node.next:
                if curr_node.data == next_node.data:
                    next_node = next_node.next
                else:
                    break
            if curr_node.data == next_node.data:
                curr_node.next = None
                break
            else:
                curr_node.next = next_node
                curr_node = curr_node.next
    return head
