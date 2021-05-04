class MyTestCase(unittest.TestCase):
    def test_something(self):
        got = Solution().levelOrderBottom(
            TreeNode(val=3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))))
        want = [[15, 7], [9, 20], [3]]
        self.assertEqual(want, got)

    def test_something(self):
        got = Solution().levelOrderBottom(
            TreeNode(val=1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5))))
        want = [[4, 5], [2, 3], [1]]
        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
