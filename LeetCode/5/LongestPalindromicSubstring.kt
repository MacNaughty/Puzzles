class Solution {
    fun longestPalindrome(s: String): String {

        if (s.isEmpty() || s.length == 1) {
            return s
        }
        val sCharArray = s.toCharArray()

        var min_start = 0
        var max_stop = 0
        for (currentIndex in sCharArray.indices) {
            if (sCharArray.lastIndex - currentIndex > max_stop - min_start) {
                for (stopIndex in currentIndex..sCharArray.lastIndex) {
                    if (max_stop - min_start < stopIndex - currentIndex) {
                        var i = currentIndex
                        var j = stopIndex
                        while ((i < j) && (sCharArray[j] == sCharArray[i])) {
                            i++
                            j--
                        }
                        if (i >= j) {
                            min_start = currentIndex
                            max_stop = stopIndex
                        }
                    }
                }
            }
        }


        return s.substring(min_start, max_stop+1)
    }
}
