class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current:
            n = current.next

            if n is None:
                break
            if n.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next