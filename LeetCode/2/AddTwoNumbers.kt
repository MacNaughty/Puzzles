/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 *
 * class ListNode(var `val`: Int) {
 *   var next: ListNode? = null
 * }
 */

class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var resultNodeCount = 0
        var resultHeadNode: ListNode? = null
        var currentResultNode: ListNode? = null

        if ((l1 != null) && (l2 != null)) {
            var carryOver = 0
            var nodeDigitSum = l1.`val` + l2.`val`
            currentResultNode = if (nodeDigitSum > 9) {
                carryOver = 1
                ListNode(nodeDigitSum.rem(10))
            } else {
                ListNode(l1.`val` + l2.`val`)
            }

            resultHeadNode = currentResultNode

            var currentFirstNode: ListNode = l1
            var currentSecondNode: ListNode = l2

            while (currentFirstNode.next != null && currentSecondNode.next != null) {
                val nextFirstNode = currentFirstNode.next ?: break
                val nextSecondNode = currentSecondNode.next ?: break
                nodeDigitSum = nextFirstNode.`val` + nextSecondNode.`val`
                val newTotalSum = carryOver + nodeDigitSum
                val nextResultNode: ListNode = if (newTotalSum > 9) {
                    carryOver = 1
                    ListNode(newTotalSum.rem(10))
                } else {
                    carryOver = 0
                    ListNode(newTotalSum)
                }

                currentResultNode?.next = nextResultNode

                currentResultNode = nextResultNode

                currentFirstNode = nextFirstNode
                currentSecondNode = nextSecondNode

            }
            if (currentFirstNode.next == null) {
                while (currentSecondNode.next != null) {
                    val nextSecondNode = currentSecondNode.next ?: break
                    val newTotalSum = carryOver + nextSecondNode.`val`

                    val nextResultNode: ListNode = if (newTotalSum > 9) {
                        carryOver = 1
                        ListNode(newTotalSum.rem(10))
                    } else {
                        carryOver = 0
                        ListNode(newTotalSum)
                    }

                    currentResultNode?.next = nextResultNode

                    currentResultNode = nextResultNode

                    currentSecondNode = nextSecondNode
                }

                if (carryOver == 1) {
                    currentResultNode?.next = ListNode(1)
                }
                return resultHeadNode
            } else {
                while (currentFirstNode.next != null) {
                    val nextFirstNode = currentFirstNode.next ?: break
                    val newTotalSum = carryOver + nextFirstNode.`val`

                    val nextResultNode: ListNode = if (newTotalSum > 9) {
                        carryOver = 1
                        ListNode(newTotalSum.rem(10))
                    } else {
                        carryOver = 0
                        ListNode(newTotalSum)
                    }

                    currentResultNode?.next = nextResultNode

                    currentResultNode = nextResultNode

                    currentFirstNode = nextFirstNode
                }
                if (carryOver == 1) {
                    currentResultNode?.next = ListNode(1)
                }
                return resultHeadNode
            }


        } else if (l1 == null) {
            return l2
        } else {
            return l1
        }
    }
}
