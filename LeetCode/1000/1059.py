from collections import defaultdict


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # bfs
        que = [source]

        edge_from_node = defaultdict(list)
        for s, d in edges:
            edge_from_node[s].append(d)

        for _ in range(n):
            next_que = []
            while que:
                node = que.pop()
                if len(edge_from_node[node]) == 0:
                    if node != destination:
                        return False
                else:
                    for ne in edge_from_node[node]:
                        if ne not in next_que:
                            next_que.append(ne)
            que = next_que
        return len(que) == 0
