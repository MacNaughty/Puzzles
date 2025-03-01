class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = deque([root])
        while q:
            curr_node = q.pop()
            res.append(curr_node.val)
            if curr_node.right:
                q.append(curr_node.right)
            if curr_node.left:
                q.append(curr_node.left)

        return res


class TestCase(unittest.TestCase):

    def test1_preorderTraversal(self):
        test_input = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual([1, 2, 3], Solution().preorderTraversal(test_input))

    def test2_preorderTraversal(self):
        test_input = TreeNode(1, TreeNode(4, TreeNode(2)), TreeNode(3))
        self.assertEqual([1, 4, 2, 3], Solution().preorderTraversal(test_input))

    def test3_preorderTraversal(self):
        test_input = TreeNode(3, TreeNode(1), TreeNode(2))
        self.assertEqual([3, 1, 2], Solution().preorderTraversal(test_input))


if __name__ == '__main__':
    unittest.main()
