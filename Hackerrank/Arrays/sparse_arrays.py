import unittest

def matchingStrings(stringList: list[str], queries: list[str]):
    res = []


    for q in queries:
        acc = 0
        for string in stringList:
            if string == q:
                acc += 1
        res.append(acc)


    return res



class MyTestCase(unittest.TestCase):
    def test_1(self):
        expected = [1, 0, 1]

        input_str_list = [
            'def',
            'de',
            'fgh',
        ]

        input_queries = [
            'de'
            'lmn'
            'fgh'
        ]

        actual = matchingStrings(input_str_list, input_queries)

        self.assertEqual(len(expected), len(actual))

        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i])

if __name__ == '__main__':
    unittest.main()
