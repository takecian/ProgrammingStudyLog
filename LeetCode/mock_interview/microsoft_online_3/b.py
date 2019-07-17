class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = 0
        while l1:
            val1 = val1 * 10 + l1.val
            l1 = l1.next

        val2 = 0
        while l2:
            val2 = val2 * 10 + l2.val
            l2 = l2.next

        ans = list(map(int, list(str(val1 + val2))))
        dummy = ListNode(0)
        current = dummy
        for a in ans:
            node = ListNode(a)
            current.next = node
            current = current.next

        return dummy.next
