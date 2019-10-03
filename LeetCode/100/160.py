# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        aset = set()
        cursor = headA
        while cursor:
            aset.add(cursor)
            cursor = cursor.next

        cursor = headB
        while cursor:
            if cursor in aset:
                return cursor
            cursor = cursor.next
        return None