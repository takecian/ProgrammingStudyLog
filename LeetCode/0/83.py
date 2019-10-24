# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        uniq_pointer = head

        cursor = head.next
        while cursor:
            if uniq_pointer.val != cursor.val:
                uniq_pointer.next = cursor
                uniq_pointer = cursor
            else:
                uniq_pointer.next = None

            cursor = cursor.next

        return head
