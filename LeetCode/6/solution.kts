class Solution {

    fun convert(s: String, numRows: Int): String {
        val sLength = s.length
        if (numRows == 1 || sLength <= numRows) {
            return s
        }

        val sCharArray: CharArray = s.toCharArray()
        val stringBuilder = StringBuilder()

        val factor = 2 * (numRows - 1)
        for (rowIndex in 0 until numRows) {
            for (i in sCharArray.indices) {
                val remainder = i % factor
                if ((remainder == rowIndex) || (remainder == factor - rowIndex)) {
                    stringBuilder.append(sCharArray[i])
                }
            }
        }

        return stringBuilder.toString()
    }
}