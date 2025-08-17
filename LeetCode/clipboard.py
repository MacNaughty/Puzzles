import unittest



class MyTestCase(unittest.TestCase):
    def test_1(self):
        print(f'1 << 2: {1 << 2}')
        print(f'1 << 3: {1 << 3}')
        print(f'1 << 4: {1 << 4}')
        self.assertEqual(1 << 4, 16)


if __name__ == '__main__':
    unittest.main()
