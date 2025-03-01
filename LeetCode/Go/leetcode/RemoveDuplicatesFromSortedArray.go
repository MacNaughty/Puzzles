package leetcode

func removeDuplicates(nums []int) int {
	numsLength := len(nums)

	if numsLength == 0 {
		return 0
	}

	newIndex := 0
	oldIndex := 1

	for oldIndex < numsLength {
		if nums[newIndex] == nums[oldIndex] {
			oldIndex++
		} else {
			nums[newIndex+1] = nums[oldIndex]
			newIndex++
			oldIndex++
		}
	}

	return newIndex + 1
}
