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


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        starts = []
        ends = []
        for n, s, e in trips:
            starts.append((s, n))
            ends.append((e, n))

        starts.sort(key=lambda x: x[0])
        ends.sort(key=lambda x: x[0])

        i = 0
        j = 0
        n = len(trips)
        passengers = 0
        while i < n and j < n:
            s_time, s_n = starts[i]
            e_time, e_n = ends[j]
            if s_time <= e_time:
                passengers += s_n
                i += 1

            if s_time >= e_time:
                passengers -= e_n
                j += 1

            if passengers > capacity:
                return False

        return True
