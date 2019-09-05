class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.size = size
        self.position = -1

    def next(self, val: int) -> float:
        if len(self.array) < self.size:
            self.array.append(val)
            self.position += 1
        else:
            self.position = (self.position + 1) % self.size
            self.array[self.position] = val

        # print(self.array)
        return sum(self.array) / len(self.array)
