class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        val nums1Size = nums1.size
        val nums2Size = nums2.size
        val resultArray = IntArray(nums1Size + nums2Size)
        var resultIndex = 0
        var firstIndex = 0
        var secondIndex = 0

        while (firstIndex < nums1Size && secondIndex < nums2Size) {//
            val firstNumber = nums1[firstIndex]
            val secondNumber = nums2[secondIndex]
            if (firstNumber < secondNumber) {
                resultArray[resultIndex] = firstNumber
                firstIndex++
            } else {
                resultArray[resultIndex] = secondNumber
                secondIndex++
            }
            resultIndex++
        }
        while (firstIndex < nums1Size) {
            resultArray[resultIndex] = nums1[firstIndex]
            firstIndex++
            resultIndex++
        }
        while (secondIndex < nums2Size) {
            resultArray[resultIndex] = nums2[secondIndex]
            secondIndex++
            resultIndex++
        }
        return when {
            resultIndex == 0 -> {
                0.0
            }
            resultIndex == 1 -> {
                resultArray[0].toDouble()
            }
            resultIndex % 2 == 0 -> {
                (resultArray[resultIndex / 2 - 1] + resultArray[resultIndex/ 2]) / 2.0
            }
            else -> {
                resultArray[resultIndex / 2].toDouble()
            }
        }
    }
}
