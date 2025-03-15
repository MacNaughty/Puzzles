import unittest


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_bst_util(node, min_value, max_value):
    if node is None:
        return True
        # The current node's value must be within the valid range
    if not (min_value < node.data < max_value):
        return False

    # Recursively check left and right subtrees with updated constraints
    return (is_bst_util(node.left, min_value, node.data) and
            is_bst_util(node.right, node.data, max_value))

def check_binary_search_tree_(root):
    return is_bst_util(root, float('-inf'), float('inf'))

class MyTestCase(unittest.TestCase):
    def test_1(self):

        actual = check_binary_search_tree_(Node(3, left=Node(5, left=Node(1), right=Node(4)), right=Node(2, left=Node(6))))
        self.assertEqual(False, actual)

    def test_2(self):

        actual = check_binary_search_tree_(Node(1, left=Node(2, left=Node(3), right=Node(4)), right=Node(2, left=Node(6))))
        self.assertEqual(False, actual)