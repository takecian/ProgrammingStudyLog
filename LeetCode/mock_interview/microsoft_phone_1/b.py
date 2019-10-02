class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.que = [0] * k
        self.k = k
        self.front = None
        self.rear = None

    def count(self):
        if self.front is None:
            return 0
        if self.front <= self.rear:
            return self.rear - self.front + 1
        return self.k + self.rear - self.front + 1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count() == self.k:
            return False

        if self.rear is None:
            self.rear = -1
            self.front = 0

        self.rear = (self.rear + 1) % self.k
        self.que[self.rear] = value
        # print(self.count(), self.front, self.rear, self.que)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count() == 0:
            return False

        count = self.count()
        if count == 1:
            self.front = None
            self.rear = None
        else:
            self.front = (self.front + 1) % self.k
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count() == 0:
            return -1
        return self.que[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count() == 0:
            return -1
        return self.que[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count() == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count() == self.k