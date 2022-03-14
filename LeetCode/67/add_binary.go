/*
https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
*/


/*
Solution 2: IMO more elegant than Solution 1
Same time & space complexity, O(n), O(n)

1. Ensure that the length of string 'a' is not less than b (by swapping assignment, if needed)
2. Make result byte slice from 'a', which has length >= string 'b'
3. Add strings together (only by incrementing result[aLastIndex-i] if b[bLastIndex-i] == 49)
4. Handle overflows from step 3
5. Handle final overflow by appending '1' to the front (left) of result []byte if needed

*/
func addBinary(a string, b string) string {
	// 	1. Ensure that the length of string 'a' is not less than b (by swapping assignment, if needed)
	if len(b) > len(a) {
		a, b = b, a
	}

	// 	2. Make result byte slice from 'a', which has length >= string 'b'
	result := []byte(a)

	aLastIndex := len(result) - 1
	bLastIndex := len(b) - 1

	// 	3. Add strings together by incrementing result[aLastIndex-i] if b[bLastIndex-i] == 49
	for i := 0; i <= bLastIndex; i++ {
		if b[bLastIndex-i] == 49 {
			result[aLastIndex-i]++
		}
	}

	// 	4. Handle carries
	for i := aLastIndex; i > 0; i-- {
		switch result[i] {
		case 51:	// carry from step 3 as well as i+1
			result[i] = 49
			result[i-1]++
		case 50:	// carry from step 3
			result[i] = 48
			result[i-1]++
		}
	}

	// 	5. Handle final carry if needed
	switch result[0] {
	case 51:	// carry from both step 3 and step 4
		result[0] = 49
		result = append([]byte{49}, result...)
	case 50:	// carry from one of step 3 and step 4
		result[0] = 48
		result = append([]byte{49}, result...)
	}

	return string(result)
}



/*
Solution 1: O(n) time complexity, O(n) space complexity

1. Handle base cases
2. cache len(a) and len(b) for making result []byte
	then for iterating right to left over both
3. Add strings from RTL, carrying a '1' when needed
4. In case len(a) != len(b) finish building result
5. Return result (with result[0] removed unless it's '1')

*/
func addBinary(a string, b string) string {
	// 1. Handle base cases
	if a == "0" {
		return b
	}
	if b == "0" {
		return a
	}

	// 2. cache len(a) and len(b) for making result []byte
	// 	then for iterating right to left over both
	aLastIndex := len(a)
	bLastIndex := len(b)

	// result length is 1 larger than greater of len(a) or len(b),
	//  in case a carry '1' is needed
	var resultLastIndex int
	if aLastIndex < bLastIndex {
		resultLastIndex = bLastIndex + 1
	} else {
		resultLastIndex = aLastIndex + 1
	}

	result := make([]byte, resultLastIndex)

	aLastIndex--
	bLastIndex--
	resultLastIndex--
	i := 0

	// 3. Add strings from RTL, carrying a '1' when needed
	carry := false
	for aLastIndex-i >= 0 && bLastIndex-i >= 0 {
		if carry {
			if a[aLastIndex-i] == '0' && b[bLastIndex-i] == '0' {
				result[resultLastIndex-i] = '1'
				carry = false
			} else if a[aLastIndex-i] == '0' || b[bLastIndex-i] == '0' {
				result[resultLastIndex-i] = '0'
			} else {
				result[resultLastIndex-i] = '1'
			}
		} else {
			if a[aLastIndex-i] == '0' {
				result[resultLastIndex-i] = b[bLastIndex-i]
			} else if b[bLastIndex-i] == '0' {
				result[resultLastIndex-i] = '1' // a[lenA-i] == '1' from previous case a[aLastIndex-i] == '0' false
			} else {
				result[resultLastIndex-i] = '0'
				carry = true
			}
		}
		i++
	}


	// 4. In case len(a) != len(b) finish building result
	finishResult := func(aOrB string, lastIndex int) {
		finishResultNoCarry := func(aOrB string, lastIndex int) {
			for lastIndex-i >= 0 {
				result[resultLastIndex-i] = aOrB[lastIndex-i]
				i++
			}
		}

		if carry {
			for lastIndex-i >= 0 {
				if aOrB[lastIndex-i] == '0' {
					result[resultLastIndex-i] = '1'
					i++
					carry = false
					break
				} else {
					result[resultLastIndex-i] = '0'
				}
				i++
			}
			finishResultNoCarry(aOrB, lastIndex)
		} else {
			finishResultNoCarry(aOrB, lastIndex)
		}

		// Add final carry, if needed
		if carry {
			result[0] = '1'
		}
	}

	
	if aLastIndex > bLastIndex {
		finishResult(a, aLastIndex)
	} else if aLastIndex < bLastIndex {
		finishResult(b, bLastIndex)
	}


	// 5. Return result (with result[0] removed unless it's '1')
	if result[0] != '1' {
		return string(result[1:])
	} else {
		return string(result)
	}
}
