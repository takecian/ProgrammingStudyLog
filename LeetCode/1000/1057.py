from collections import defaultdict
import heapq


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distance_list = defaultdict(list)
        for i in range(len(workers)):
            wx, wy = workers[i]
            for j in range(len(bikes)):
                bx, by = bikes[j]
                dis = abs(wx - bx) + abs(wy - by)
                distance_list[i].append((dis, i, j))
            distance_list[i].sort(reverse=True)

        used_bikes = set()
        ans = [0] * len(workers)
        queue = [distance_list[i].pop() for i in range(len(workers))]  # smallest distance for each worker
        heapq.heapify(queue)

        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(queue)
            if bike not in used_bikes:
                ans[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distance_list[worker].pop())  # bike used, add next closest bike

        return ans
