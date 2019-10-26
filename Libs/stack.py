class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        node = ListNode(item)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        return node.val

    def peek(self):
        if self.is_empty():
            return None
        return self.head.val


if __name__ == '__main__':
    q = Stack()
    q.push(10)
    q.push(20)
    print(q.pop())
    print(q.pop())
    q.push(30)
    q.push(40)
    q.push(50)
    print(q.peek())
    print(q.pop())
    print(q.pop())
    print("popd item is " + str(q.pop()))