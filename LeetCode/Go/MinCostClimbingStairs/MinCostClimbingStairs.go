/*
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.


Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
*/

// Helper function (for both solutions)
func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}


// Solution 3:
// Similar idea as solution 1, but uses far less memory because it's caching the minimum number of steps (2) necessary to calculate the cost of the next one
// Time complexity O(n), space complexity O(1)
func minCostClimbingStairs(cost []int) int {
	even := cost[0]
	odd := cost[1]

	for i := 2; i < len(cost); i++ {
    // bitwise check for even/odd
		if i&1 == 0 {
			even = cost[i] + min(even, odd)
		} else {
			odd = cost[i] + min(even, odd)
		}
	}

	return min(even, odd)
}


// Solution 1:
// For each step, calculate the minimum possible cost to get there (based on a comparison of the last two steps)
// Time complexity O(n), space complexity O(n)
func minCostClimbingStairs(cost []int) int {
	costLength := len(cost)
	if costLength == 2 {
		return min(cost[0], cost[1])
	}

	dp := make([]int, costLength)
	dp[0] = cost[0]
	dp[1] = cost[1]

	for i := 2; i < costLength; i++ {
		dp[i] = cost[i] + min(dp[i-1], dp[i-2])
	}

	if dp[costLength-1] > dp[costLength-2] {
		return dp[costLength-2]
	} else {
		return dp[costLength-1]
	}
}
