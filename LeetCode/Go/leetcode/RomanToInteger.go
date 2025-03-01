package leetcode

//import "fmt"

//func main() {
//	fmt.Printf("Converted CML to %d", romanToInt("CML"))
//}

// Solution 1: romanNumeral struct; based off of quii tutorials; to test understanding
//func romanToInt1(s string) int {
//	stringLength := len(s)
//	result := 0
//
//	for i := 0; i < stringLength; i++ {
//		currentByte := s[i]
//		if i+1 < stringLength {
//			if isSubtractiveNumeral(currentByte) {
//				potentialDifferenceNumeral := s[i : i+2]
//				differenceNumeralResult := searchDifferenceNumeralsGivenString(potentialDifferenceNumeral)
//				if differenceNumeralResult != 0 {
//					result += differenceNumeralResult
//					i++
//					continue
//				}
//			}
//		}
//		result += symbolToInt(currentByte)
//	}
//
//	return result
//}

type romanNumeral struct {
	Symbol string
	Value  int
}

type RomanNumerals []romanNumeral

var allRomanNumerals = RomanNumerals{
	{"I", 1},
	{"V", 5},
	{"X", 10},
	{"L", 50},
	{"C", 100},
	{"D", 500},
	{"M", 1000},
}

func symbolToInt(b byte) int {
	for _, rN := range allRomanNumerals {
		if rN.Symbol[0] == b {
			return rN.Value
		}
	}
	return 0
}

var subtractiveNumerals = RomanNumerals{
	{"I", 1},
	{"X", 10},
	{"C", 100},
}

func isSubtractiveNumeral(b byte) bool {
	for _, char := range subtractiveNumerals {
		if b == char.Symbol[0] {
			return true
		}
	}
	return false
}

//var differenceNumerals = RomanNumerals{
//	{"IV", 4},
//	{"IX", 9},
//	{"XL", 40},
//	{"XC", 90},
//	{"CD", 400},
//	{"CM", 900},
//}

//func searchDifferenceNumeralsGivenString(s string) int {
//	for _, rN := range differenceNumerals {
//		if rN.Symbol == s {
//			return rN.Value
//		}
//	}
//	return 0
//}

// Solution 2: Using maps instead of structs
func romanToInt2(s string) int {

	result := 0
	stringLength := len(s)

	for i := 0; i < stringLength; i++ {
		currByte := s[i]
		if i+1 < stringLength {
			subtractiveNumeralValue := differenceNumerals[currByte][s[i+1]]
			if subtractiveNumeralValue != 0 {
				result += subtractiveNumeralValue
				i++
				continue
			}
		}
		result += allSingleCharacters[currByte]
	}
	return result
}

var allSingleCharacters = map[byte]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

var differenceNumerals = map[byte]map[byte]int{
	'I': {
		'V': 4,
		'X': 9,
	},
	'X': {
		'L': 40,
		'C': 90,
	},
	'C': {
		'D': 400,
		'M': 900,
	},
}

// Solution 3: best solution; single map iterating RTL to determine subtractive numerals
func romanToInt3(s string) int {
	stringLength := len(s)
	sum := 0
	lastVal := 0
	romanMap := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

	for i := stringLength - 1; i >= 0; i-- {
		val := romanMap[s[i]]
		if val >= lastVal {
			sum += val
		} else {
			sum -= val
		}
		lastVal = val
	}

	return sum
}
