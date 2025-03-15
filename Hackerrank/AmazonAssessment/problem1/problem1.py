import unittest

def countPossibleWinners(initialRewards):
    max_initial_points = -1

    # collect canditates
    for i in range(len(initialRewards)):
        if initialRewards[i] > max_initial_points:
            max_initial_points = initialRewards[i]

    candidates = []
    for i in range(len(initialRewards)):
        if initialRewards[i] >= max_initial_points - 1:
            candidates.append(i)

    return len(candidates)


# def countPossibleWinners(initialRewards):
#     total_customers = len(initialRewards)
#
#     max_initial_points = -1
#     initial_rewards_dict = {}
#
#     # collect canditates
#     for i in range(len(initialRewards)):
#         initial_rewards_dict[i] = initialRewards[i]
#         if initialRewards[i] > max_initial_points:
#             max_initial_points = initialRewards[i]
#
#     initialRewards.sort()
#
#     candidates = []
#     for i in range(len(initialRewards)):
#         if initial_rewards_dict[i] + total_customers > max_initial_points + total_customers - 1:
#             candidates.append(i)
#
#     return len(candidates)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = [8, 10, 9]
        expected = 2
        actual = countPossibleWinners(input)


        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        input = [5, 7, 9, 11]
        expected = 1
        actual = countPossibleWinners(input)


        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()


list(map(int, "2 9 6 4 1 3 7 5 11 8 10".split()))
