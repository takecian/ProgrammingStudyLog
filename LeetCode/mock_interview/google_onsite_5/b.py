import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        workers_num = len(workers)
        bikes_num = len(bikes)

        worker_bikes_pairs = []
        for i in range(workers_num):
            worker_bikes_pair = []
            worker = workers[i]
            for j in range(bikes_num):
                bike = bikes[j]
                worker_bikes_pair.append((abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]), i, j))
            worker_bikes_pair.sort(reverse=True)
            worker_bikes_pairs.append(worker_bikes_pair)

        used_bikes = set()
        ans = [0] * workers_num

        queue = [worker_bikes_pairs[i].pop() for i in range(workers_num)]  # smallest distance for each worker

        heapq.heapify(queue)
        while len(used_bikes) < workers_num:
            _, w, b = heapq.heappop(queue)
            if b not in used_bikes:
                ans[w] = b
                used_bikes.add(b)
            else:
                heapq.heappush(queue, worker_bikes_pairs[w].pop())
        return ans
