
// splitting string and taking last element (too much work at the beginning)
func lengthOfLastWord(s string) int {
	wordSlice := strings.Split(s, " ")

	for i := len(wordSlice) - 1; i >= 0; i-- {
		if wordSlice[i] != "" {
			return len(wordSlice[i])
		}
	}

	return 0
}
