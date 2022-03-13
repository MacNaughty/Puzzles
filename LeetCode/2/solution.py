class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    @classmethod
    def add_rem(cls, l: Optional[ListNode], curr_node: ListNode, carry: int) -> [ListNode, ListNode, int]:

        res_sum = l.val + carry
        if res_sum == 0 and l.next is None:
            return
        if res_sum >= 10:
            carry = int(res_sum / 10)
            res_sum = res_sum % 10
        else:
            carry = 0

        curr_node.next = ListNode(res_sum)
        l = l.next

        curr_node = curr_node.next

        return l, curr_node, carry

    @classmethod
    def add_two_numbers(cls, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        curr_node = head

        # initialize
        res_sum = l1.val + l2.val
        if res_sum == 0 and l1.next is None and l2.next is None:
            return head
        if res_sum >= 10:
            carry = int(res_sum / 10)
            res_sum = res_sum % 10

        curr_node.val = res_sum
        l1 = l1.next
        l2 = l2.next

        while l1 is not None and l2 is not None:
            
            res_sum = l1.val + l2.val + carry

            if res_sum >= 10:
                carry = int(res_sum / 10)
                res_sum = res_sum % 10
            else:
                carry = 0

            curr_node.next = ListNode(res_sum)
            curr_node = curr_node.next

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            l1, curr_node, carry = Solution.add_rem(l1, curr_node, carry)

        while l2 is not None:
            l2, curr_node, carry = Solution.add_rem(l2, curr_node, carry)

        if carry != 0:
            curr_node.next = ListNode(carry)

        return head


class TestCase(unittest.TestCase):

    def test_helper(self, l: ListNode):
        res = []
        while l:
            res.append(l.val)
            l = l.next

        return res

    def test_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))

        expected = ListNode(7, ListNode(0, ListNode(8)))
        self.assertEqual(self.test_helper(expected), self.test_helper(Solution.add_two_numbers(l1, l2)))

    def test_2(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

        # expected = ListNode(1, ListNode(0, ListNode(0, ListNode(0, ListNode(9, ListNode(9, ListNode(9, ListNode(8))))))))
        expected = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
        self.assertEqual(self.test_helper(expected), self.test_helper(Solution.add_two_numbers(l1, l2)))

    def test_3(self):
        l1 = ListNode(2, ListNode(4, ListNode(9)))
        l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))

        expected = ListNode(7, ListNode(0, ListNode(4, ListNode(0, ListNode(1)))))
        self.assertEqual(self.test_helper(expected), self.test_helper(Solution.add_two_numbers(l1, l2)))

    def test_4(self):
        l1 = ListNode(1, ListNode(6, ListNode(0, ListNode(3, ListNode(3, ListNode(6, ListNode(7, ListNode(2, ListNode(0, ListNode(1))))))))))
        l2 = ListNode(6, ListNode(3, ListNode(0, ListNode(8, ListNode(9, ListNode(6, ListNode(6, ListNode(9, ListNode(6, ListNode(1))))))))))

        expected = ListNode(7, ListNode(9, ListNode(0, ListNode(1, ListNode(3, ListNode(3, ListNode(4, ListNode(2, ListNode(7, ListNode(2))))))))))

        self.assertEqual(self.test_helper(expected), self.test_helper(Solution.add_two_numbers(l1, l2)))

    def test_5(self):
        l1 = ListNode(0, ListNode(8, ListNode(8, ListNode(8, ListNode(8, ListNode(2, ListNode(9, ListNode(3, ListNode(1, ListNode(1))))))))))
        l2 = ListNode(0, ListNode(9, ListNode(1, ListNode(5, ListNode(5, ListNode(5, ListNode(1, ListNode(1, ListNode(6)))))))))

        expected = ListNode(0, ListNode(7, ListNode(0, ListNode(4, ListNode(4, ListNode(8, ListNode(0, ListNode(5, ListNode(7, ListNode(1))))))))))

        self.assertEqual(self.test_helper(expected), self.test_helper(Solution.add_two_numbers(l1, l2)))

    def test_6(self):
        l1 = ListNode(3, ListNode(2, ListNode(0, ListNode(2, ListNode(6, ListNode(0, ListNode(8, ListNode(8, ListNode(0, ListNode(1))))))))))
        l2 = ListNode(0, ListNode(8, ListNode(9, ListNode(6, ListNode(8, ListNode(7, ListNode(2)))))))

        expected = ListNode(3, ListNode(0, ListNode(0, ListNode(9, ListNode(4, ListNode(8, ListNode(0, ListNode(9, ListNode(0, ListNode(1))))))))))

        self.assertEqual(self.test_helper(expected), self.test_helper(Solution.add_two_numbers(l1, l2)))
