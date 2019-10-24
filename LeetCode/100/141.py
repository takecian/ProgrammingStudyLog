# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = set()
        cursor = head
        while cursor is not None:
            if cursor in nodes:
                return True
            nodes.add(cursor)
            cursor = cursor.next
        return False