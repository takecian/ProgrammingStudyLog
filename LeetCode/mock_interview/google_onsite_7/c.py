from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        edges = defaultdict(list)
        for i in range(len(stones) - 1):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    edges[i].append(j)
                    edges[j].append(i)
        ans = 0
        visited = set()

        for i in range(len(stones)):
            if i in visited:
                continue

            ans += 1
            que = [i]
            visited.add(i)
            while que:
                stone = que.pop()

                for next in edges[stone]:
                    if next not in visited:
                        que.append(next)
                        visited.add(next)
        return len(stones) - ans