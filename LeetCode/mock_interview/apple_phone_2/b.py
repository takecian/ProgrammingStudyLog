class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        time = 0
        for trip in trips:
            time = max(time, trip[2])

        capacity_log = [0] * (time + 1)
        for n, s, e in trips:
            capacity_log[s] += n
            capacity_log[e] -= n
        for i in range(1, len(capacity_log)):
            capacity_log[i] += capacity_log[i - 1]
            if capacity_log[i] > capacity:
                return False
        return True
