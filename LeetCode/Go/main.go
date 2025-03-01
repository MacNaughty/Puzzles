package main

import (
	"fmt"
	"go_leetcode_module/leetcode"
)

func main() {
	//nums := []int{2, 7, 11, 15}
	numStairs := 2
	//target := 9
	result := leetcode.ClimbStairs(numStairs)
	fmt.Println("ClimbStairs output", result)
}
