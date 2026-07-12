import unittest
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        num_set = set(nums)

        while num_set:
            current_streak = 1
            num = num_set.pop()
            curr = num - 1
            while curr in num_set:
                num_set.remove(curr)
                current_streak += 1
                curr -= 1

            curr = num + 1
            while curr in num_set:
                num_set.remove(curr)
                current_streak += 1
                curr += 1

            max_streak = max(max_streak, current_streak)

        return max_streak


    def longestConsecutive_timeout(self, nums: List[int]) -> int:
        """
        ASSUMPTIONS:
        :param nums: can contain duplicates
        :return:
        """
        if not nums:
            return 0

        streaks: list[tuple] = [(nums[0], nums[0])]

        for num in nums[1:]:
            has_match = False
            is_dup = False
            for i in range(len(streaks)):
                start, stop = streaks[i]
                if start <= num <= stop:
                    is_dup = True
                    has_match = True
                    break

                if num == start - 1:
                    streaks[i] = start - 1, stop
                    has_match = True
                    break
                if num == stop + 1:
                    streaks[i] = start, stop + 1
                    has_match = True
                    break

            if is_dup:
                continue

            if has_match:
                for i in range(len(streaks)-1):
                    if streaks[i][1] + 1 >= streaks[i+1][0]:
                        _, stop = streaks.pop(i+1)
                        streaks[i] = streaks[i][0], stop
                        break
            else:
                if not streaks or num > streaks[-1][1]:
                    streaks.append((num, num))
                elif num < streaks[0][0]:
                    streaks.insert(0, (num, num))
                else:
                    index = -1
                    for i in range(len(streaks) - 1):
                        low_start, low_stop = streaks[i]
                        high_start, high_stop = streaks[i+1]
                        if low_stop < num < high_start:
                            index = i+1
                            break

                    if index != -1:
                        streaks.insert(index, (num, num))

        max_streak = 1
        for streak in streaks:
            max_streak = max(abs(streak[1] - streak[0])+1, max_streak)

        return max_streak






class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [100,4,200,1,3,2]
        expected = 4
        actual = Solution().longestConsecutive_timeout(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        expected = 9
        actual = Solution().longestConsecutive_timeout(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [1,0,1,2]
        expected = 3
        actual = Solution().longestConsecutive_timeout(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [1,2,6,7,8]
        expected = 3
        actual = Solution().longestConsecutive_timeout(nums)
        self.assertEqual(expected, actual)

    def test_5(self):
        nums = [9,1,4,7,3,-1,0,5,8,-1,6]
        expected = 7
        actual = Solution().longestConsecutive_timeout(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
