# Definition for singly-linked linked_list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)

        zero = dummy
        first = None

        cursor = head
        while cursor:
            if not first:
                first = cursor
                cursor = cursor.next
            else:
                second = cursor
                zero.next = second
                cursor = cursor.next
                second.next = first
                first.next = cursor
                zero = first
                first = None

        return dummy.next
