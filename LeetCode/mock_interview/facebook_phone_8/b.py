class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        que = collections.deque()
        cursor = head
        while cursor:
            node = cursor
            cursor = cursor.next
            node.next = None
            que.append(node)

        dummy = ListNode(0)
        ans = dummy

        is_even = True
        while len(que) > 0:
            if is_even:
                node = que.popleft()
                is_even = False
            else:
                node = que.pop()
                is_even = True
            ans.next = node
            ans = ans.next

        return dummy.next
