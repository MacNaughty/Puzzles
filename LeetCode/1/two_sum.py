class Solution:
  
  
# solutiotion 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {1: 1}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

        return None
      
# solution 2: two pass hash table
# Time complexity O(n), space complexity O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            cache[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if cache.__contains__(complement) and cache[complement] != i:
                return cache[complement], i

        return None

      
      
# solution 3: one pass hash table 
# Time complexity O(n), space complexity O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in cache:
                return cache[complement], i
            cache[nums[i]] = i

        return None
