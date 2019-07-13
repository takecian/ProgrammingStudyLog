class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)

        c1 = l1
        c2 = l2
        carry = 0
        cursor = dummy
        while c1 and c2:
            val = c1.val + c2.val + carry

            carry = val // 10
            val = val % 10
            cursor.next = ListNode(val)
            cursor = cursor.next
            c1 = c1.next
            c2 = c2.next

        rest = c1 if c1 else c2
        while rest:
            val = rest.val + carry
            carry = val // 10
            val = val % 10
            cursor.next = ListNode(val)
            cursor = cursor.next
            rest = rest.next

        if carry:
            cursor.next = ListNode(carry)

        return dummy.next