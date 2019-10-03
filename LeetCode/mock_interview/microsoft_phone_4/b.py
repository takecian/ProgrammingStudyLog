# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        first = head
        second = head.next
        while first and second:
            n_prev = first
            n_first = second.next
            if second.next:
                n_second = second.next.next
            else:
                n_second = None

            prev.next = second
            first.next = second.next
            second.next = first

            prev = n_prev
            first = n_first
            second = n_second

        return dummy.next