# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        p1 = dummy
        p2 = dummy
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        latter = p1.next
        sorted_p = self.sortList(latter)
        p1.next = None
        return self.merge(self.sortList(head), sorted_p)

    def merge(self, h1, h2):
        dummy = ListNode(0)
        cursor = dummy
        while h1 and h2:
            # print(h1, h2)
            if h1.val < h2.val:
                cursor.next = h1
                h1 = h1.next
            else:
                cursor.next = h2
                h2 = h2.next
            cursor = cursor.next

        if h1:
            cursor.next = h1
        if h2:
            cursor.next = h2
        return dummy.next

