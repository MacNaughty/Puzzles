class Solution:
  
    # Solution 1:  Time complexity O(n), Space complexity O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in cache:
                return cache[complement]+1, i+1
            cache[numbers[i]] = i
            
    # Solution 2:  Time complexity O(n), Space complexity O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while i < j:
        if numbers[i] + numbers[j] == target:
            return i+1, j+1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
