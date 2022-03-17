class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        for (i in nums.indices) {
            for (j in (i + 1) until nums.size) {
                val valI = nums[i]
                val valJ = nums[j]
                if (valI + valJ == target) return intArrayOf(i, j)
            }
        }
        return intArrayOf(0 , 1)
    }
}
