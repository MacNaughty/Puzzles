import unittest

def countArray(n, k, x):
    MOD = 10**9 + 7  # Required by the problem statement
    # initialize array with zeros
    mem = [[0] * k for _ in range(n)]

    # only one way to make array of length 1:
    #       it has to end with 1
    mem[0][0] = 1

    for i in range(1,n):
        for j in range(k):
            mem[i][j] = sum(mem[i-1]) - mem[i-1][j]

    return mem[n-1][x-1] % (MOD)


def countArray_v1(n, k, x):
    MOD = 10**9 + 7  # Required by the problem statement
    # initialize array with zeros
    mem = [0] * k
    # first iteration corresponds to array of length 1,
    # only one way to make array of length 1 that ends in 1
    mem[0] = 1

    for i in range(1,n):
        mem = [sum(mem) - x for x in mem]
    return mem[x-1] % (MOD)

def countArray_v2(n, k, x):
    MOD = 10**9 + 7
    mem = [1,0]

    for i in range(1,n):
        mem[0], mem[1] = (k - 1) * mem[1], mem[0] + (k - 2) * mem[1]

    ans = mem[0] if x == 1 else mem[1]
    return ans % (MOD)



class MyTestCase(unittest.TestCase):
    def test_1(self):
        n = 4
        k = 3
        x = 2
        expected = 3
        actual = countArray(n, k, x)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
