// Time complexity O(n), space complexity O(n)

var twoSum = function(nums, target) {

    const cache = {}
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]
        if (complement in cache) {
            return [cache[complement], i]
        }
        cache[nums[i]] = i
    }
}
