package main

import (
	"fmt"
	countandsay "go_leetcode_module/38"
)

func main() {
	//nums := []int{2, 7, 11, 15}
	numStairs := 6
	//target := 9
	result := countandsay.CountAndSay(numStairs)
	fmt.Println("CountAndSay output", result)
}
