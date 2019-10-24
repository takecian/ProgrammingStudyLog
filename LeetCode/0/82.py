# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        answer_cursor = dummy

        cursor = head
        while cursor:
            if cursor.next is None or cursor.val != cursor.next.val:
                answer_cursor.next = cursor
                answer_cursor = answer_cursor.next

            current_val = cursor.val
            while cursor and cursor.val == current_val:
                cursor = cursor.next

            answer_cursor.next = None

        return dummy.next

