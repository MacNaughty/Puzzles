package leetcode

// https://leetcode.com/problems/climbing-stairs/submissions/

// Solved the problem by hand, realized it was equivalent to the fibbonaci sequence
func ClimbStairs(n int) int {
	if n < 4 {
		return n
	}

	n -= 3

	lastValue := 2
	currValue := 3

	for n > 0 {
		currValue = lastValue + currValue
		lastValue = currValue - lastValue
		n--
	}

	return currValue
}
