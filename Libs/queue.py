
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        node = ListNode(item)

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.is_empty():
            return None

        temp = self.head
        self.head = temp.next

        if self.head is None:
            self.tail = None

        return temp.val


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q.dequeue())
    print(q.dequeue())
    print("Dequeued item is " + str(q.dequeue()))