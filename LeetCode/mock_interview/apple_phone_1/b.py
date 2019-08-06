import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.length = 0
        cursor = head
        while cursor:
            self.length += 1
            cursor = cursor.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        rand = random.randint(0, self.length - 1)
        cursor = self.head
        while rand > 0:
            # print(rand)
            cursor = cursor.next
            # print(cursor)
            rand -= 1
        return cursor.val