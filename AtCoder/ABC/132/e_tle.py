#
from collections import deque

import sys

def main():
    n, m = map(int, input().split())

    edges = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges[u].append(v)
    # print(edges)

    s, t = map(int, input().split())

    def next_kenp(node):
        nodes = set()
        nodes2 = set()

        for n1 in edges[node]:
            for n2 in edges[n1]:
                if n2 not in nodes2:
                    nodes2.add(n2)

        for nn in nodes2:
            for n3 in edges[nn]:
                if n3 in dones or n3 in nodes:
                    continue
                nodes.add(n3)
        return nodes

    dones = set()
    que = deque()
    que.append((s, 0))
    while que:
        node, step = que.popleft()
        next_nodes = next_kenp(node)
        for n in next_nodes:
            if n == t:
                print(step + 1)
                exit()

            que.append((n, step + 1))
            dones.add(n)

    print(-1)


if __name__ == '__main__':
    main()
