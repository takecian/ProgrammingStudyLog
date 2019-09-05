# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        cursor = ans
        carry = 0
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = add // 10
            add = add % 10
            cursor.next = ListNode(add)
            cursor = cursor.next

            l1 = l1.next
            l2 = l2.next

        rest_node = l1 if l1 else l2
        if rest_node:
            while rest_node:
                add = rest_node.val + carry
                carry = add // 10
                add = add % 10
                cursor.next = ListNode(add)
                cursor = cursor.next
                rest_node = rest_node.next

        if carry:
            cursor.next = ListNode(carry)

        return ans.next