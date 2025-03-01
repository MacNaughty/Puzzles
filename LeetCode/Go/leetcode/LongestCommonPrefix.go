package leetcode

import "strings"

func longestCommonPrefix(strs []string) string {
	strsLength := len(strs)

	if strsLength == 0 {
		return ""
	}

	var result strings.Builder

	j := 0

	for len(strs[0]) > j {
		byteToCheck := strs[0][j]

		for i := 1; i < strsLength; i++ {
			if len(strs[i]) <= j || byteToCheck != strs[i][j] {
				return result.String()
			}
		}
		result.WriteByte(byteToCheck)
		j++
	}

	return result.String()
}
