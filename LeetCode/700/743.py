from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        inf = 10 ** 10
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        visited = set()
        ans = 0

        q = []
        heappush(q, (0, K))
        while q:
            cost, node = heappop(q)
            if node in visited:
                continue
            visited.add(node)
            ans = max(ans, cost)

            for v, w in edges[node]:
                if v in visited:
                    continue
                heappush(q, (cost + w, v))

        return ans if len(visited) == N else -1