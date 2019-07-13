# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cursor = dummy

        c1 = l1
        c2 = l2
        while c1 and c2:
            if c1.val < c2.val:
                cursor.next = c1
                c1 = c1.next
            else:
                cursor.next = c2
                c2 = c2.next

            cursor = cursor.next

        rest = c1 if c1 else c2
        if rest:
            cursor.next = rest

        return dummy.next