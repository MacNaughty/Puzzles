package countandsay

import (
	"strconv"
	"strings"
)

func CountAndSay(n int) string {
	if n == 1 {
		return "1"
	}

	var currTerm = "11"
	for i := 1; i < n-1; i++ {
		var newTerm strings.Builder
		var prevIndex = 0

		for currIndex := 0; currIndex < len(currTerm); currIndex++ {
			if currTerm[prevIndex] != currTerm[currIndex] {
				newTerm.WriteString(strconv.Itoa(currIndex - prevIndex))
				newTerm.WriteByte(currTerm[prevIndex])
				if currIndex+1 == len(currTerm) {
					newTerm.WriteString("1")
					newTerm.WriteByte(currTerm[currIndex])
				} else {
					prevIndex = currIndex
				}
			} else if currIndex+1 == len(currTerm) {
				newTerm.WriteString(strconv.Itoa(currIndex - prevIndex + 1))
				newTerm.WriteByte(currTerm[currIndex])
			}
		}
		currTerm = newTerm.String()
	}

	return currTerm

}

// Cleaner solution (from Leetcode)
func countAndSay(n int) string {

	currTerm := "1"
	if n == 1 {
		return currTerm
	}
	for i := 2; i <= n; i++ {
		nextTerm := strings.Builder{}
		prevIndex := 0
		currIndex := 0
		for currIndex < len(currTerm) {
			if currTerm[currIndex] == currTerm[prevIndex] {
				currIndex++
			} else {
				nextTerm.WriteString(strconv.Itoa(currIndex - prevIndex))
				nextTerm.WriteByte(currTerm[prevIndex])
				prevIndex = currIndex
			}
		}
		nextTerm.WriteString(strconv.Itoa(currIndex - prevIndex))
		nextTerm.WriteByte(currTerm[prevIndex])
		currTerm = nextTerm.String()
	}

	return currTerm
}
