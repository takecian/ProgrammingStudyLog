class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        index = timestamp % 300
        if self.ts[index] != timestamp:
            self.ts[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        ans = 0
        for i in range(300):
            if timestamp - self.ts[i] < 300:
                ans += self.hits[i]
        return ans

    # Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)