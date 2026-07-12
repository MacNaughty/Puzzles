import unittest
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next

    return res

def assert_equal(node1, node2):
    linked_list1 = get_list(node1)
    linked_list2 = get_list(node2)
    print(f'linked_list1: {linked_list1}')
    print(f'linked_list2: {linked_list2}')

    if len(linked_list1) != len(linked_list2):
        return False

    for i in range(len(linked_list1)):
        if linked_list1[i] != linked_list2[i]:
            return False

    return True

    # if node1 is None and node2 is None:
    #     return True
    # while node1.next and node2.next:
    #     if node1.val != node2.val:
    #         return False
    #     node1 = node1.next
    #     node2 = node2.next
    #
    # if not node1.next and node2.next:
    #     return False
    # if node1.next and not node2.next:
    #     return False
    #
    # return True


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        len_lists = len(lists)
        if len_lists == 0:
            return None

        root = None

        first_nonempty_index = -1
        for i in range(0, len_lists):
            if lists[i]:
                root = lists[i]
                first_nonempty_index = i
                break

        if not root:
            return root

        for i in range(first_nonempty_index + 1, len_lists):
            if lists[i] is None:
                continue

            # begin integrating existing result (starting with root) with the current sublist
            new_node = lists[i]

            while new_node:
                if root.next is None:
                    root.next = new_node
                    break
                elif new_node.val <= root.val:
                    root = ListNode(new_node.val, root)
                elif new_node.val <= root.next.val:
                    root.next = ListNode(new_node.val, root.next)
                else:
                    old_node = root.next
                    is_last = False
                    while old_node:
                        if old_node.next is None:
                            old_node.next = new_node
                            is_last = True
                            break
                        elif new_node.val <= old_node.next.val:
                            old_node.next = ListNode(new_node.val, old_node.next)
                            break
                        else:
                            old_node = old_node.next

                    if is_last:
                        break

                new_node = new_node.next

        return root


class MyTestCase(unittest.TestCase):
    def test_1(self):
        lists = []
        self.assertTrue(assert_equal(Solution().mergeKLists(lists), None))  # add assertion here

    def test_2(self):
        lists = [[]]
        self.assertTrue(assert_equal(Solution().mergeKLists(lists), None))  # add assertion here

    def test_3(self):
        lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6)), ]
        self.assertTrue(assert_equal(Solution().mergeKLists(lists), ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))))  # add assertion here

    def test_4(self):
        lists = [ListNode(0), ListNode(1)]
        self.assertTrue(assert_equal(Solution().mergeKLists(lists), ListNode(0, ListNode(1))))  # add assertion here

    def test_5(self):
        lists = [ListNode(1, ListNode(2, ListNode(3))), ListNode(4, ListNode(5, ListNode(6, ListNode(7))))]
        self.assertTrue(assert_equal(Solution().mergeKLists(lists), ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, )))))))))  # add assertion here

    def test_6(self):
        lists = [ListNode(2), None, ListNode(-1)]
        self.assertTrue(assert_equal(Solution().mergeKLists(lists), ListNode(-1, ListNode(2))))  # add assertion here


if __name__ == '__main__':
    unittest.main()
