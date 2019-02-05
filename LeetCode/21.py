# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        head = None
        head1 = l1
        head2 = l2
        if not head1 and head2:
            head = ListNode(head2.val)
            head2 = head2.next
        elif head1 and not head2:
            head = ListNode(head1.val)
            head1 = head1.next

        if head1 and head2:
            if head1.val < head2.val:
                head = ListNode(head1.val)
                head1 = head1.next
            else:
                head = ListNode(head2.val)
                head2 = head2.next
        top = head
        while head1 or head2:
            if not head1:
                head.next = ListNode(head2.val)
                head = head.next
                head2 = head2.next
            elif not head2:
                head.next = ListNode(head1.val)
                head = head.next
                head1 = head1.next
            else:
                if head1.val < head2.val:
                    head.next = ListNode(head1.val)
                    head = head.next
                    head1 = head1.next
                else:
                    head.next = ListNode(head2.val)
                    head = head.next
                    head2 = head2.next
        return top

s = Solution()
s.mergeTwoLists()
