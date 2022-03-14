func lengthOfLastWord(s string) int {
	acc := 0
	lastIndex := len(s) - 1

	for i := lastIndex; i >= 0; i-- {
		if s[i] != ' ' {
			acc++
		} else {
			if acc != 0 {
				break
			}
		}
	}

	return acc
}


// splitting string and taking last element
func lengthOfLastWord(s string) int {
	wordSlice := strings.Split(s, " ")

	for i := len(wordSlice) - 1; i >= 0; i-- {
		if wordSlice[i] != "" {
			return len(wordSlice[i])
		}
	}

	return 0
}
