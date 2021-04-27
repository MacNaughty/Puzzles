/*
https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.


Solution 1: Handle base cases, allocate memory for result, build result from right to left by adding strings 'a' and 'b' together with carry when needed
O(n) time complexity, O(n) space complexity
*/
func addBinary1(a string, b string) string {
	if a == "0" {
		return b
	}
	if b == "0" {
		return a
	}

	lenA := len(a)
	lenB := len(b)

	var resultLength int
	if lenA < lenB {
		resultLength = lenB + 1
	} else {
		resultLength = lenA + 1
	}

	result := make([]byte, resultLength)

	lenA--
	lenB--
	resultLength--
	i := 0

	carry := false
	for lenA-i >= 0 && lenB-i >= 0 {
		if carry {
			if a[lenA-i] == '0' && b[lenB-i] == '0' {
				result[resultLength-i] = '1'
				carry = false
			} else if a[lenA-i] == '0' || b[lenB-i] == '0' {
				result[resultLength-i] = '0'
			} else {
				result[resultLength-i] = '1'
			}
		} else {
			if a[lenA-i] == '0' && b[lenB-i] == '0' {
				result[resultLength-i] = '0'
			} else if a[lenA-i] == '0' || b[lenB-i] == '0' {
				result[resultLength-i] = '1'
			} else {
				result[resultLength-i] = '0'
				carry = true
			}
		}
		i++
	}
	for lenA-i >= 0 {
		if carry {
			if a[lenA-i] == '0' {
				result[resultLength-i] = '1'
				carry = false
			} else {
				result[resultLength-i] = '0'
			}
		} else {
			result[resultLength-i] = a[lenA-i]
		}
		i++
	}
	for lenB-i >= 0 {
		if carry {
			if b[lenB-i] == '0' {
				result[resultLength-i] = '1'
				carry = false
			} else {
				result[resultLength-i] = '0'
			}
		} else {
			result[resultLength-i] = b[lenB-i]
		}
		i++
	}
	if carry {
		result[0] = '1'
	}
	if result[0] != '0' && result[0] != '1' {
		return string(result[1:])
	} else {
		return string(result)
	}
}


/*
Solution 2: ensure that length of string 'a' is not less than b, make result byte slice from 'a', 
then add all bytes from 'b' (again, from right to left)
Time complexity O(n), space complexity O(n)

*/

func addBinary(a string, b string) string {
	if len(b) > len(a) {
		a, b = b, a
	}

	result := []byte(a)

	aLastIndex := len(result) - 1
	bLastIndex := len(b) - 1

	for i := 0; i <= bLastIndex; i++ {
		result[aLastIndex-i] += b[bLastIndex-i]
	}

  /*
  In addition to the 4 cases that result from adding the bytes '0' (48) and '1' (49), 
  we consider the 4 possible sums of the two (96, 97, 98)
  as well as the overflows from carry increments; 48-49 and 96-97 makes no difference, 
  but 49->50 is like two '1's (i.e. 98) and 98->99 becomes its own case
  
  */
	for i := aLastIndex; i > 0; i-- {
		switch result[i] {
		case 98, 50:
			result[i] = 48
			result[i-1]++
		case 99:
			result[i] = 49
			result[i-1]++
		case 97:
			result[i] = 49
		case 96:
			result[i] = 48
		}
	}

	switch result[0] {
	case 99:
		result[0] = 49
		result = append([]byte{49}, result...)
	case 98, 50:
		result[0] = 48
		result = append([]byte{49}, result...)
	case 97:
		result[0] = 49
	case 96:
		result[0] = 48
	}

	return string(result)

}
