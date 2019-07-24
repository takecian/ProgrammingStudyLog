# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        nodes.sort()

        head = dummy = ListNode(0)
        for node in nodes:
            head.next = ListNode(node)
            head = head.next

        return dummy.next