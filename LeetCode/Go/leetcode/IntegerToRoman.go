package leetcode

import "strings"

// First solution: arrays of roman numeral structs grouped by the number of digits they represent
//func intToRoman(num int) string {
//
//	var digitCount = getDigitCount(num)
//
//	result := make([]string, digitCount)
//	for x := 0; x < digitCount; x++ {
//		if x == digitCount-1 {
//			if digitCount == 4 {
//				result[x] = getRomanNumeralFourthDigit(num)
//			} else {
//				result[x] = getRomanNumeralGivenBaseAndTarget(x, num)
//			}
//			break
//		} else {
//			result[x] = getRomanNumeralGivenBaseAndTarget(x, num%10)
//		}
//
//		num /= 10
//	}
//
//	return strings.Join(result, "")
//}

func getRomanNumeralFourthDigit(target int) string {
	var tempBuilder strings.Builder
	acc := 0
	for target > acc {
		tempBuilder.WriteString("M")
		acc++
	}
	return tempBuilder.String()
}

//func getRomanNumeralGivenBaseAndTarget(baseX int, target int) (digitAsNumeralString string) {
//	numeralSlice := digitArrayMap[baseX]
//
//	for _, numeral := range numeralSlice {
//		if numeral.value == target {
//			digitAsNumeralString = numeral.symbol
//			break
//		} else if numeral.value < target {
//			var tempBuilder strings.Builder
//			tempBuilder.WriteString(numeral.symbol)
//			acc := numeral.value
//			for target > acc {
//				tempBuilder.WriteString(numeralSlice[3].symbol)
//				acc++
//			}
//			digitAsNumeralString = tempBuilder.String()
//			break
//		}
//	}
//	return
//}

func getDigitCount(num int) (digitCount int) {
	switch {
	case num >= 1000:
		digitCount = 4
	case num >= 100:
		digitCount = 3
	case num >= 10:
		digitCount = 2
	default:
		digitCount = 1
	}
	return
}

//type romanNumeral struct {
//	symbol string
//	value  int
//}

type romanNumeralArray [4]romanNumeral

var singleDigitArray = romanNumeralArray{
	{"IX", 9},
	{"V", 5},
	{"IV", 4},
	{"I", 1},
}

var doubleDigitArray = romanNumeralArray{
	{"XC", 9},
	{"L", 5},
	{"XL", 4},
	{"X", 1},
}

var tripleDigitArray = romanNumeralArray{
	{"CM", 9},
	{"D", 5},
	{"CD", 4},
	{"C", 1},
}

// digitArrayMap[x] givens roman numerals relevant for digit (i.e. 10^x)
var digitArrayMap = map[int]romanNumeralArray{
	0: singleDigitArray,
	1: doubleDigitArray,
	2: tripleDigitArray,
}

// Second solution: basically same as above, using map[int]string instead of romanNumeral struct
//func intToRoman(num int) string {
//
//	var digitCount = getDigitCount(num)
//
//	result := make([]string, digitCount)
//	currDigit := 1
//	for i := digitCount - 1; i >= 0; i-- {
//		if digitCount == 4 && i == 0 {
//			result[i] = getRomanNumeralForThousandDigit(num)
//		} else if i != 0 {
//			result[i] = getRomanNumeralForDigit(currDigit, num%10)
//		} else {
//			result[i] = getRomanNumeralForDigit(currDigit, num)
//		}
//
//		num /= 10
//		currDigit++
//	}
//
//	return strings.Join(result, "")
//}

func getRomanNumeralForThousandDigit(target int) string {
	var tempBuilder strings.Builder
	acc := 0
	for target > acc {
		tempBuilder.WriteString("M")
		acc++
	}
	return tempBuilder.String()
}

var digitNumeralMapKeys = [4]int{9, 5, 4, 1}

func getRomanNumeralForDigit(currDigit int, target int) (digitAsString string) {
	digitNumeralMap := digitNumeralSliceMap[currDigit]

	for _, value := range digitNumeralMapKeys {
		if value == target {
			digitAsString = digitNumeralMap[value]
			break
		} else if value < target {
			var tempBuilder strings.Builder
			tempBuilder.WriteString(digitNumeralMap[value])
			acc := value
			for target > acc {
				tempBuilder.WriteString(digitNumeralMap[1])
				acc++
			}
			digitAsString = tempBuilder.String()
			break
		}
	}
	return
}

//func getDigitCount(num int) (digitCount int) {
//	switch {
//	case num >= 1000:
//		digitCount = 4
//	case num >= 100:
//		digitCount = 3
//	case num >= 10:
//		digitCount = 2
//	default:
//		digitCount = 1
//	}
//	return
//}

var singleDigitNumeralSlice = map[int]string{
	9: "IX",
	5: "V",
	4: "IV",
	1: "I",
}

var doubleDigitNumeralSlice = map[int]string{
	9: "XC",
	5: "L",
	4: "XL",
	1: "X",
}

var tripleDigitNumeralSlice = map[int]string{
	9: "CM",
	5: "D",
	4: "CD",
	1: "C",
}

var digitNumeralSliceMap = map[int]map[int]string{
	1: singleDigitNumeralSlice,
	2: doubleDigitNumeralSlice,
	3: tripleDigitNumeralSlice,
}
