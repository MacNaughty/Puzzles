class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        if (s.isEmpty()) {
        return 0
    }
        var longestSubstring = "${s[0]}"
    var currentSubstring: String = "${s[0]}"
    for (i in 0 until s.length - 1) {
        val nextChar = s[i + 1]
        if (currentSubstring.contains(nextChar)) {
            if (currentSubstring.length > longestSubstring.length) {
                longestSubstring = currentSubstring
            }
            val newStartingIndex: Int = currentSubstring.indexOfFirst { c: Char -> c == nextChar }
            currentSubstring = currentSubstring.substring(newStartingIndex + 1, currentSubstring.length) + nextChar

        } else {
            currentSubstring += nextChar
        }

    }

    return if (currentSubstring.length > longestSubstring.length) {
        currentSubstring.length
    } else {
        longestSubstring.length
    }
    }
}
