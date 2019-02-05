# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        head1 = l1
        head2 = l2

        top = head
        while head1 and head2:
            if head1.val < head2.val:
                head.next = ListNode(head1.val)
                head = head.next
                head1 = head1.next
            else:
                head.next = ListNode(head2.val)
                head = head.next
                head2 = head2.next

        if head1:
            head.next = head1

        if head2:
            head.next = head2

        return top.next

s = Solution()
s.mergeTwoLists()
