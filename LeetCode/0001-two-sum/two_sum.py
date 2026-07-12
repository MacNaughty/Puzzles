class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 2], Solution.two_sum([3, 2, 4], 6))

    def test_2(self):
        self.assertEqual([0, 1], Solution.two_sum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    unittest.main()

class Solution:
      
    # solution 1: two pass hash table
    # Time complexity O(n), space complexity O(n)
    @classmethod
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            cache[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if cache.__contains__(complement) and cache[complement] != i:
                return cache[complement], i

        return None

      
      
    # solution 2: one pass hash table 
    # Time complexity O(n), space complexity O(n)
    @classmethod
    def two_sum(cls, nums: List[int], target: int) -> List[int]:
        complement_index_dict = {}
    
        for i, num in enumerate(nums):
            if num in complement_index_dict:
                return [i, complement_index_dict[num]]
    
            complement_index_dict[target - num] = i

        return None
      
      
      
   
