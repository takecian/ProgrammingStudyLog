
#

import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop

def main():
    n, m, p = map(int, input().split())
    graph = defaultdict(list)
    coins = {}
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1].append(b-1)
        coins[(a-1,b-1)] = -(c - p)

    inf = 10**10
    scores = [inf] * n
    scores[0] = 0
    # bellman-ford
    for loop in range(2):
        for i in range(n):
            for next_node in graph[i]:
                scores[next_node] = min(scores[next_node], scores[i] + coins[(i, next_node)])

        if loop == 0:
            ans = scores[-1]

    print(-1 if ans != scores[-1] or ans == inf else -ans)  # n 回移動した時点よりスコアが良くなってたら無限に上げられる


if __name__ == '__main__':
    main()
