class MyTestCase(unittest.TestCase):
    def test_something(self):
        got = Solution().subsets([1, 2, 3])
        want = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
