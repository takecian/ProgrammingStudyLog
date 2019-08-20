# https://atcoder.jp/contests/abc137/tasks/abc137_e

import sys
sys.setrecursionlimit(12345678)
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n, m, p = map(int, input().split())
    edges = []
    graph = defaultdict(list)
    rev_graph = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        c = -(c - p)
        edges.append((a, b, c))
        graph[a].append(b)
        rev_graph[b].append(a)

    # pick up nodes on goal path
    reachable_from_start = [False] * n

    # print(edges)
    def dfs(node):
        if reachable_from_start[node]:
            return
        reachable_from_start[node] = True
        for next_node in graph[node]:
            dfs(next_node)

    reachable_to_end = [False] * n

    def rdfs(node):
        if reachable_to_end[node]:
            return
        reachable_to_end[node] = True
        for next_node in rev_graph[node]:
            rdfs(next_node)

    dfs(0)
    rdfs(n-1)

    valid = [False] * n
    for i in range(n):
        valid[i] = reachable_from_start[i] and reachable_to_end[i]

    inf = 10**10
    scores = [inf] * n
    scores[0] = 0
    loop = 0

    # bellman-ford
    updated = True
    while updated:
        updated = False
        for i in range(m):
            a, b, c = edges[i]
            if not valid[a]:
                continue
            if not valid[b]:
                continue

            new_cost = scores[a] + c
            if new_cost < scores[b]:
                updated = True
                scores[b] = new_cost

        loop += 1
        if loop > n:
            print(-1)
            return

    print(max(0, -scores[-1]))


if __name__ == '__main__':
    main()
