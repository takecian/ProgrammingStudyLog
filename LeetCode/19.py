# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        before = top = head
        for _ in range(n):
            top = top.next

        if top == None:
            return head.next

        while top.next != None:
            top = top.next
            before = before.next

        before.next = before.next.next
        return head
