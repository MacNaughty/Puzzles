import unittest
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyTestCaseHelper(unittest.TestCase):

    def assert_list_nodes_equal(self, expected, actual):
        while expected and actual:
            self.assertEqual(expected.val, actual.val)
            expected = expected.next
            actual = actual.next

        self.assertTrue(expected and actual or (not expected and not actual))

    def assert_expected_list_contains_tree(self, expected: list, actual: TreeNode):
        actual_list = self.tree_to_list(actual)
        while actual_list[-1] is None:
            actual_list.pop()

        self.assertEqual(expected, actual_list)
        # expected_tuple_set = set([tuple(e) for e in expected])
        # self.assertIn(actual_list, expected_tuple_set)

    def assert_list_equals_tree(self, expected_list, actual_tree_root):
        actual_list = self.tree_to_list(actual_tree_root)
        for i in range(len(expected_list)):
            self.assertEqual(expected_list[i], actual_list[i])

    def tree_to_list(self, root):
        res = [root.val]

        stack = [root]
        while stack:
            node = stack.pop(0)

            res.append(node.left.val if node.left else None)
            if node.left:
                stack.append(node.left)

            res.append(node.right.val if node.right else None)
            if node.right:
                stack.append(node.right)

        return res

    def array_to_binary_tree(self, arr):
        if not arr:
            return None

        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1

        while i < len(arr):
            current = queue.popleft()

            if i < len(arr):
                if arr[i] is not None:
                    current.left = TreeNode(arr[i])
                    queue.append(current.left)
                i += 1

            if i < len(arr):
                if arr[i] is not None:
                    current.right = TreeNode(arr[i])
                    queue.append(current.right)
                i += 1

        return root

    def assert_two_d_lists_equal(self, expected, actual):
        self.assertEqual(len(expected), len(actual))

        expected_tuples = set([tuple(element) for element in expected])
        for element in actual:
            element_set = tuple(element)
            self.assertIn(element_set, expected_tuples)

    def linked_list_to_array(self, head):
        if not head:
            return []

        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res


    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
