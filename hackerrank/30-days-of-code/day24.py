# https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head==None:
            return head

        cursor = head
        uniq = head
        current = head.data
        while cursor:
            while cursor and cursor.data == current:
                cursor = cursor.next

            # print(cursor.data)
            uniq.next = cursor
            uniq = uniq.next
            if uniq:
                current = uniq.data
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);