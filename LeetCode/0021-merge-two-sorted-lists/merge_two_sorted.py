
# Solution 1: Time complexity O(n + m), Space complexity O(n + m)
class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        head = None
        curr_node = None
        if l1.val <= l2.val:
            head = l1
            curr_node = l1
            l1 = l1.next
        else:
            head = l2
            curr_node = l2
            l2 = l2.next
        while l1 and l2:
            if l1.val <= l2.val:
                curr_node.next = l1
                curr_node = curr_node.next
                l1 = l1.next
            else:
                curr_node.next = l2
                curr_node = curr_node.next
                l2 = l2.next

        if l1:
            curr_node.next = l1
        if l2:
            curr_node.next = l2

        return head

    
    
# Same time and space complexity, O(n + m), but more concise
class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        curr_node = ListNode(val=None, next=None)
        fake_head = curr_node

        while l1 and l2:
            if l1.val <= l2.val:
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next

        if l1:
            curr_node.next = l1
        if l2:
            curr_node.next = l2

        return fake_head.next
