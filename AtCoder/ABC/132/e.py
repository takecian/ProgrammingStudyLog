#
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, m = map(int, input().split())

    edges = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        edges[(u, 0)].append((v, 1))
        edges[(u, 1)].append((v, 2))
        edges[(u, 2)].append((v, 0))

    s, t = map(int, input().split())

    # print(new_edges)

    dones = set()
    que = deque()
    que.append(((s, 0), 0))
    while que:
        node, step = que.popleft()

        next_nodes = edges[node]
        # print(next_nodes)
        for n, l in next_nodes:
            if n == t and l == 0:
                print((step + 1) // 3)
                exit()

            if (n, l) not in dones:
                que.append(((n, l), step + 1))
                dones.add((n, l))
    print(-1)


if __name__ == '__main__':
    main()
