import unittest

class Solution2:
    def inorder_traversal(self, indexes, node, result):
        """Performs in-order traversal on the tree represented as an array."""
        if node == -1:
            return
        left, right = indexes[node - 1]  # Get left and right children
        self.inorder_traversal(indexes, left, result)
        result.append(node)  # Visit current node
        self.inorder_traversal(indexes, right, result)

    def swap_subtrees(self, indexes, node, depth, k):
        """Swaps the left and right children of nodes at depth multiples of k."""
        if node == -1:
            return
        i = node - 1
        if depth % k == 0:
            indexes[i][0], indexes[i][1] = indexes[i][1], indexes[i][0]
        left, right = indexes[i]  # Get left and right children
        self.swap_subtrees(indexes, left, depth + 1, k)
        self.swap_subtrees(indexes, right, depth + 1, k)

    def swapNodes(self, indexes, queries):
        results = []
        for k in queries:
            self.swap_subtrees(indexes, 1, 1, k)  # Start at root node (1) with depth = 1
            result = []
            self.inorder_traversal(indexes, 1, result)  # Collect in-order traversal
            results.append(result)
        return results


class Solution1:
    class TreeNode:
        def __init__(self, value, depth):
            self.value = value
            self.depth = depth
            self.left = None
            self.right = None

    def build_tree(self, indexes):
        nodes = {1: self.TreeNode(1, 1)}
        for i, (left, right) in enumerate(indexes):
            current = nodes[i + 1]
            if left != -1:
                nodes[left] = self.TreeNode(left, current.depth + 1)
                current.left = nodes[left]
            if right != -1:
                nodes[right] = self.TreeNode(right, current.depth + 1)
                current.right = nodes[right]
        return nodes[1]

    def swap_subtrees(self, node, k):
        if node is None:
            return
        if node.depth % k == 0:
            node.left, node.right = node.right, node.left
        self.swap_subtrees(node.left, k)
        self.swap_subtrees(node.right, k)

    def inorder_traversal(self, node: TreeNode, result):
        if node is None:
            return
        self.inorder_traversal(node.left, result)
        result.append(node.value)
        self.inorder_traversal(node.right, result)
        return result

    def swapNodes(self, indexes, queries):
        root = self.build_tree(indexes)
        results = []
        for k in queries:
            self.swap_subtrees(root, k)
            result = self.inorder_traversal(root, [])
            results.append(result)
        return results


class MyTestCase(unittest.TestCase):
    def test_1(self):

        actual = Solution1().swapNodes(
            [
                    [2, 3],
                    [-1, -1],
                    [-1, -1]
                   ],
            [1, 1]
        )

        expected = [
            [3, 1, 2],
            [2, 1, 3],
        ]

        for i in range(len(actual)):
            for j in range(len(actual[i])):
                self.assertEqual(actual[i][j], expected[i][j])

    def test_2(self):
        input = [
            [2 , 3],
            [4 , 5],
            [6 , -1],
            [-1,  7],
            [8 , 9],
            [10,  11],
            [12,  13],
            [-1,  14],
            [-1,  -1],
            [15,  -1],
            [16,  17],
            [-1,  -1],
            [-1,  -1],
            [-1,  -1],
            [-1,  -1],
            [-1,  -1],
            [-1,  -1],
        ]
        actual = Solution1().swapNodes(
            input,
            [2, 3]
        )

        expected = [
            [14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16],
            [9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15],
        ]

        for i in range(len(actual)):
            for j in range(len(actual[i])):
                self.assertEqual(actual[i][j], expected[i][j])

    def test_3(self):
        input = [[2 , 3],
        [4 , -1],
        [5 , -1],
        [6 , -1],
        [7 , 8],
        [-1,  9],
        [-1,  -1],
        [10,  11],
        [-1,  -1],
        [-1,  -1],
        [-1,  -1]]

        actual = Solution1().swapNodes(
            input,
            [2, 4]
        )

        expected = [
            list(map(int, "2 9 6 4 1 3 7 5 11 8 10".split())),
            list(map(int, "2 6 9 4 1 3 7 5 10 8 11".split()))
        ]

        for i in range(len(actual)):
            for j in range(len(actual[i])):
                self.assertEqual(actual[i][j], expected[i][j])


if __name__ == '__main__':
    unittest.main()
