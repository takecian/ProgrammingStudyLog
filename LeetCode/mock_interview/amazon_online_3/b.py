class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.window = [0] * size
        self.pos = 0

    def next(self, val: int) -> float:
        self.window[self.pos] = val
        self.pos = (self.pos + 1) % len(self.window)
        if self.count < len(self.window):
            self.count += 1

        return sum(self.window[:self.count]) / self.count
